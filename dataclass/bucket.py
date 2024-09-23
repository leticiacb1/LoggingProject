import json
import boto3
import io

from config.config import Config

class Bucket():

    def __init__(self):
        self.s3_client = None

        # Load environment variables
        self.config = Config()
        self.config.load()

    def create(self, bucket_name : str) -> None:    
        
        self.s3_client = boto3.client( "s3",
                                        aws_access_key_id=self.config.ACCESS_KEY,
                                        aws_secret_access_key=self.config.SECRET_KEY,
                                        region_name=self.config.REGION
                                    )
        
        self.s3_client.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={"LocationConstraint": self.config.REGION},
        )

        print("\n    [INFO] Create a S3 Bucket in AWS. \n")

    def write_logs(self, body: str, bucket: str, key: str) -> None:          
        self.s3_client.put_object(Body=body, Bucket=bucket, Key=key)

        print("\n    [INFO] Write log in S3 Bucket. \n")
        print("\n           > Bucket: " + bucket)
        print("\n           > Key: " +  key)
        print("\n           > Body: \n" + body)

    def check_logs(self, bucket_name: str, key: str) -> None:
        
        print("\n    [INFO] Check logs in S3 Bucket. \n")
        
        obj = self.s3_client.get_object(Bucket=bucket_name, Key=key)
        file_content = obj["Body"].read().decode("utf-8")

        print("\n           > Stored log: \n")
        print(file_content)

    def cleanup(self, bucket_name: str, key: str) -> None:
        print(f"\n    [INFO] Delete Bucket with name = {bucket_name} and key = {key}. \n")
        self.s3_client.delete_object(Bucket=bucket_name, Key=key)
