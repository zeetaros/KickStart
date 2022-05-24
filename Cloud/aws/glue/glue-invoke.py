"""
    lambda function to trigger a glue job
"""

import os
import time
import boto3
import logging
from urllib.parse import unquote_plus

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(module)s - %(message)s")
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

s3_client = boto3.client("s3")
glue_client = boto3.client("glue")

GLUE_JOB_NAME = os.getenv(key="GLUE_JOB_NAME" , default="custom_job")


def lambda_handler(event, context):
    for record in event["Records"]:
        source_bucket = record["s3"]["bucket"]["name"]
        source_key = unquote_plus(record["s3"]["object"]["key"])
        glueJobName = GLUE_JOB_NAME

        file_path = os.path.join(
            "s3://", source_bucket, "/".join(source_key.split("/")[:-1]) + "/"
        )
        file_name = source_key.split("/")[-1]

        logger.debug(
            f"arguments passed ont glue job: [input_paths={file_path}], [file_name={file_name}]"
        )

        job_done = False
        attempt = 0

        while attempt < 5 and job_done == False:
            try:
                response = glue_client.start_job_run(
                    JobName=glueJobName,
                    Arguments={"--input_paths": file_path, "--file_name": file_name},
                )
                job_done = True
                logger.info(
                    f"Glue job {glueJobName} triggered with [job_id={response['JobRunId']}]"
                )
            except glue_client.exceptions.ConcurrentRunsExceededException:
                logger.error(
                    f"ConcurrentRunsExceededException occurs when calling the StartJobRun operation: Concurrent runs exceeded for {glueJobName}"
                )
                attempt += 1
                time.sleep(10)
                logger.debug(
                    f"retrying after ConcurrentRunsExceededException. \nattempt made: {attempt}"
                )
        if job_done == False:
            logger.error(
                f"maximum retry attempt met - file(s) in [file_path={file_path}] are not processed by glue job"
            )
            raise RuntimeError(
                "maximum retry attempt met - glue job did not get triggered successfully"
            )
