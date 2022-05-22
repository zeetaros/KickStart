import sys
import logging
import traceback
import pandas as pd

from datetime import datetime, timedelta
from pyspark.sql import SQLContext
from pyspark.sql.functions import input_file_name
from pyspark.context import SparkContext

from awsglue.transforms import *
from awsglue.utils import getResolvedOptions, GlueArgumentError
from awsglue.context import GlueContext
from awsglue.job import Job
from awsglue.dynamicframe import DynamicFrame

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

logger.info("============ GLUE JOB STARTED ============")


class ValidationError(Exception):
    def __init__(self, msg):
        self.msg = msg


"""
     first off, handle case when the job is triggered by lambda functions, where arguments are expected to be passed on by the lambda function. 
     what arguments to pass on are defined within the lambda function, they could be a specific s3 file path in which the files needed to process resides. 
     
     if these arguments are not received, such as in case when the job is triggered by glue trigger, then initialise the glue job with default configurations.
"""
## Paramters received from glue invoke lambda function (if the Glue job is triggered by a lambda function)
input_paths = None
output_path = "s3://p314159-glue-files-processed/"
try:
    args = getResolvedOptions(sys.argv, ["JOB_NANME", "input_paths", "file_name"])
    input_paths = [args["input_paths"]]
    logger.debug(f"arguments received from lambda: {args}")
    logger.info(f"glue job triggered by file {args['file_name']}")
except GlueArgumentError:
    args = getResolvedOptions(sys.argv, ["JOB_NAME"])

sc = SparkContext()
sqlContext = SQLContext(sc)
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)

## Initialise the job
job.init(args["JOB_NAME"], args)
logger.info("============ JOB INITIATED ============")

if not input_paths:
    input_paths = ["s3://p314159-glue-files-staging/"]

logger.debug(f"Un-bookmarked files from [{input_paths}] will be processed")

## @type: DataSource
## @return: DataSource0
## @inputs: s3 paths
DataSource0 = glueContext.create_dynamic_frame.from_options(
    format_options={"jsonPath": "", "multiline": True},
    connection_type="s3",
    format="json",
    connection_options={"paths": input_paths},
    additional_options={"recurse": True},
    transformation_ctx="DataSource0",
)

logger.info("============ TRANSFORMATION STARTED ============")

## Create a Spark DataFrame and add a new column to fetch the s3 file name of every DataRecord
spark_df = DataSource0.toDF()
spark_df.withColumn("filename", input_file_name())

## Convert to a Pandas DataFrame
pandas_df = spark_df.toPandas()

if len(pandas_df) == 0:
    logger.warning(
        f"empty dataframe - check if new data received since last run of the job"
    )
else:
    mandatory_columns = ["id", "name"]
    for col in mandatory_columns:
        if pandas_df[col].isna().any():
            raise ValidationError(
                msg=f"Found value missing in mandatory [column={col}] in [file={pandas_df[pandas_df[col].isna()]['filename'].unique()}]"
            )
    pandas_df["checked"] = True

    ## Convert back to Spark DataFrame
    new_spark_df = sqlContext.createDataFrame(pandas_df)

    defg1 = DynamicFrame.fromDF(new_spark_df, glueContext, "defg")

    ## Determine whether to split the output into multiple files when saving
    defg1 = defg1.repartition(1)

    logger.debug(f"writing to s3 target bucket: {output_path}")
    DataSink0 = glueContext.write_dynamic_frame.from_options(
        frame=defg1,
        connection_type="s3",
        format="csv",
        connection_options={"path": output_path, "partitionKeys": []},
        transformation_ctx="DataSink0",
    )

## Bookmark is effective only when the job is committed
job.commit()
