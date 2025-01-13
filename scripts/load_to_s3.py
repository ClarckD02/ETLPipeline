import boto3
import json
import os

# Load AWS credentials from environment variables or config file
try:
    aws_access_key = os.environ["AWS_ACCESS_KEY_ID"]
    aws_secret_key = os.environ["AWS_SECRET_ACCESS_KEY"]
    aws_region = os.environ["AWS_REGION"]
    bucket_name = os.environ["AWS_BUCKET_NAME"]
except KeyError:
    # If environment variables are not set, fall back to config file
    with open("config/aws_config.json") as f:
        config = json.load(f)
    aws_access_key = config["aws_access_key"]
    aws_secret_key = config["aws_secret_key"]
    aws_region = config["aws_region"]
    bucket_name = config["bucket_name"]

# Initialize the S3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    region_name=aws_region
)

# Define the local file path
local_file_path = "data/raw_stock_data.json"
s3_key = "raw_data/raw_stock_data.json"  # Key in S3

def upload_to_s3():
    """Uploads the extracted JSON file to S3."""
    if not os.path.exists(local_file_path):
        print(f"Error: {local_file_path} not found.")
        return

    try:
        s3.upload_file(local_file_path, bucket_name, s3_key)
        print(f"Successfully uploaded {local_file_path} to s3://{bucket_name}/{s3_key}")
    except Exception as e:
        print(f"Error uploading to S3: {e}")

if __name__ == "__main__":
    upload_to_s3()
