import os
import json
import boto3
from unittest import TestCase

func_name = os.environ['FUNCTION_NAME']
ld_client = boto3.client('lambda')
eb_client = boto3.client('events')

class TestEventBridgeExercise(TestCase):
    def setUp(self) -> None:
        with open(os.path.join(os.path.dirname(__file__), './test_resources/mock_event.json'),'r') as f:
            self.expected_event_config = json.load(f)
        with open(os.path.join(os.path.dirname(__file__), './test_resources/mock_lambda.json'),'r') as f:
            self.expected_lambda_config = json.load(f)
        self.actual_lambda_config = self.get_actual_lambda_config()
        self.actual_event_config = self.get_actual_event_config()
        return super().setUp()
    
    def tearDown(self) -> None:
        return super().tearDown()

    def get_actual_lambda_config(self):
        try:
            res = ld_client.get_function(FunctionName=func_name)
            return res
        except Exception as e:
            raise e

    def get_actual_event_config(self):
        lambda_arn = self.actual_lambda_config["Configuration"]["FunctionArn"]
        try:
            eb_name_info = eb_client.list_rule_names_by_target(TargetArn=lambda_arn)
            eb_name = eb_name_info['RuleNames'][0]
            eb_pattern = eb_client.describe_rule(Name=eb_name)
            eb_dict = json.loads(eb_pattern['EventPattern'])
            return eb_dict
        except Exception as e:
            raise e

    def test_lambda_timeout(self):
        self.assertEqual(self.actual_lambda_config['Configuration']["Timeout"], 
                         self.expected_lambda_config['Configuration']["Timeout"])

    def test_lambda_env_variables(self):
        self.assertEqual(self.actual_lambda_config['Configuration']['Environment'], 
                         self.expected_lambda_config['Configuration']['Environment'])

    def test_lambda_role(self):
        self.assertEqual(self.actual_lambda_config['Configuration']['Role'], 
                         self.expected_lambda_config['Configuration']['Role'])

    def test_event_config(self):
        self.assertEqual(self.actual_event_config,
                         self.expected_event_config)