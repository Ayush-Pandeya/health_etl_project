import boto3
import os
from dotenv import load_dotenv

load_dotenv()

def upload_to_s3(local_file, s3_key):
    s3 = boto3.client('s3',
                      aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
                      aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"))
    bucket = os.getenv("S3_BUCKET_NAME")
    s3.upload_file(local_file, bucket, s3_key)
    print(f"✅ Uploaded {local_file} to s3://{bucket}/{s3_key}")