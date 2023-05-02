from datetime import datetime, time
from dagster import daily_schedule, schedule, repository
from workflow_demo import bday_pipeline

@schedule(cron_schedule="0 1 * * *", pipeline_name="bday_pipeline", execution_timezone="Europe/London")
def my_execution_time_schedule(context):
    date = context.scheduled_execution_time.strftime("%Y-%m-%d")
    return {
        "solids": {
            "get_date": {"config": {"date": date}}
        }
    }
    
@daily_schedule(
    pipeline_name="bday_pipeline",
    start_date=datetime(2021, 9, 1),
    execution_time=time(6, 45),
    execution_timezone="Europe/London",
)
def bday_schedule(date):
    return {
        "solids": {
            "get_date": {"config": {"date": date.strftime("%Y-%m-%d")}}
        }
    }

@repository
def bday_repository():
    return [bday_pipeline, bday_schedule]