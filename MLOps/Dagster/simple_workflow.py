from dagster import pipeline, solid
from sklearn.svm import SVC, LinearSVC



@solid
def make_predict(data):
    SVC

@solid
def get_name():
    return "dagster"


@solid
def hello(context, name):
    context.log.info(f"Hello, {name}!")


@pipeline
def hello_pipeline():
    hello(get_name())