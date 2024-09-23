import json
import boto3
import io

from config.config import Config

class Logs():

    def __init__(self):
    
        self.logs_client = None
        self.log_events = None

        # Load environment variables
        self.config = Config()
        self.config.load()

    def create_client(self) -> None:    
        # Initialize the AWS SDK
        session = boto3.Session(
            aws_access_key_id=self.config.ACCESS_KEY,
            aws_secret_access_key=self.config.SECRET_KEY,
            region_name=self.config.REGION
        )

        self.logs_client = session.client("logs")
        print("\n    [INFO] Create AWS CloudWatch Logs client. \n")

    def get_events(self, lambda_group_name: str) -> None:

        print(f"\n    [INFO] Get log streams from lambda_group_name = {lambda_group_name}. \n")

        # Retrieve the log streams for the Lambda function
        response = self.logs_client.describe_log_streams(
            logGroupName=lambda_group_name
        )

        # Select the desired log stream (e.g., the latest stream)
        log_stream_name = response["logStreams"][0]["logStreamName"]

        # Retrieve the log events from the selected log stream
        self.log_events = self.logs_client.get_log_events(
            logGroupName=lambda_group_name,
            logStreamName=log_stream_name,
        )

        # Process the log events
        for i, event in enumerate(self.log_events["events"]):
            # Print the log event
            print("\n           > " + event["message"])

            # Print a separator between log events
            if event != len(self.log_events["events"]) - 1:
                print("-" * 60)
                print(f"\n           > LOG {i+1}:")

            # Print the log message
            print(event["message"])
