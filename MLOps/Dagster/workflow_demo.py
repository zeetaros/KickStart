from dagster import pipeline, solid, op, job, execute_pipeline
from datetime import datetime

@op
def get_name():
    return "dagster"

@op
def get_age():
    return 19

@solid
def get_date(context):
    # date = context.solid_config["date"]
    date = datetime.now()
    return date

@op
def bday(context, name, age, date):
    context.log.info(f"Party on {date}.")
    context.log.info(f"Happy {age} birthday, {name}!")

@job
def bday_pipeline():
    bday(name=get_name(), age=get_age(), date=get_date())

if __name__ == "__main__":
    result = execute_pipeline(bday_pipeline)