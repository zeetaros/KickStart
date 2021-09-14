from dagster import pipeline, solid, execute_pipeline

@solid
def get_name():
    return "dagster"

@solid
def get_age():
    return 19

@solid
def get_date(context):
    date = context.solid_config["date"]
    return date

@solid
def bday_wish(context, name, age, date):
    context.log.info(f"Party on {date}.")
    context.log.info(f"Happy {age} birthday, {name}!")

@pipeline
def bday_pipeline():
    bday_wish(get_name(), get_age())

if __name__ == "__main__":
    result = execute_pipeline(bday_pipeline)