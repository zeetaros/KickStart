from dagster import pipeline, solid
from savable import SavableSVC


@op
def load_model(model_path):
    pass

@op
def make_predict(data, model):
    # model.predict()
    pass

@job
def run_workflow():
    # model_loaded = load_model(model_path=)
    # make_predict(data=, model=model_loaded)
    pass