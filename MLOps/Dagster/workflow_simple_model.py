from dagster import pipeline, solid
from savable import SavableSVC


@solid
def load_model(model_path):
    pass

@solid
def make_predict(data, model):
    # model.predict()
    pass

@pipeline
def run_workflow():
    # model_loaded = load_model(model_path=)
    # make_predict(data=, model=model_loaded)
    pass