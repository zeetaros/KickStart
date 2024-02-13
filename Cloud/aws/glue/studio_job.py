import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job

args = getResolvedOptions(sys.argv, ["JOB_NAME"])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args["JOB_NAME"], args)

# Script generated for node S3 bucket
S3bucket_node1 = glueContext.create_dynamic_frame.from_options(
    format_options={"jsonPath": "$[*]", "multiline": False},
    connection_type="s3",
    format="json",
    connection_options={
        "paths": ["s3://glue-demo-datasource/staging/"],
        "recurse": True,
    },
    transformation_ctx="S3bucket_node1",
)

# Script generated for node ApplyMapping
ApplyMapping_node2 = ApplyMapping.apply(
    frame=S3bucket_node1,
    mappings=[
        ("id", "int", "id", "int"),
        ("num", "string", "num", "string"),
        ("name", "string", "name", "string"),
        ("img", "string", "img", "string"),
        ("type", "array", "type", "array"),
        ("height", "string", "height", "string"),
        ("weight", "string", "weight", "string"),
        ("candy", "string", "candy", "string"),
        ("candy_count", "int", "candy_count", "int"),
        ("egg", "string", "egg", "string"),
        ("spawn_chance", "double", "spawn_chance", "double"),
        ("avg_spawns", "choice", "avg_spawns", "choice"),
        ("spawn_time", "string", "spawn_time", "string"),
        ("multipliers", "array", "multipliers", "array"),
        ("weaknesses", "array", "weaknesses", "array"),
    ],
    transformation_ctx="ApplyMapping_node2",
)

# Script generated for node Select Fields
SelectFields_node1653265330697 = SelectFields.apply(
    frame=ApplyMapping_node2,
    paths=[
        "id",
        "num",
        "name",
        "img",
        "height",
        "weight",
        "candy",
        "candy_count",
        "egg",
        "spawn_chance",
        "avg_spawns",
        "spawn_time",
    ],
    transformation_ctx="SelectFields_node1653265330697",
)

# Script generated for node S3 bucket
S3bucket_node3 = glueContext.getSink(
    path="s3://glue-demo-datasource/processed/",
    connection_type="s3",
    updateBehavior="UPDATE_IN_DATABASE",
    partitionKeys=[],
    enableUpdateCatalog=True,
    transformation_ctx="S3bucket_node3",
)

# Create a table in Glue Data Catalog
S3bucket_node3.setCatalogInfo(
    catalogDatabase="demo-dev", catalogTableName="glue-demo-table"
)
S3bucket_node3.setFormat("csv")
S3bucket_node3.writeFrame(SelectFields_node1653265330697)
job.commit()
