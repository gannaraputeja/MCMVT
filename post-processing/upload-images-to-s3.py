import boto3
import os
import sys

def upload_files_to_s3(local_folder, s3_bucket, s3_folder):
    # Create an S3 client
    s3 = boto3.client('s3')

    # Iterate over files in the local folder
    for root, dirs, files in os.walk(local_folder):
        for filename in files:
            local_path = os.path.join(root, filename)
            # Calculate the S3 key (path within the bucket)
            s3_key = os.path.join(s3_folder, os.path.relpath(local_path, local_folder))
            # Upload the file to S3
            s3.upload_file(local_path, s3_bucket, s3_key)
            print(f"Uploaded {local_path} to s3://{s3_bucket}/{s3_key}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python script.py <local_folder_path> <s3_bucket> <s3_folder>")
        sys.exit(1)
    
    local_folder = sys.argv[1]
    s3_bucket = sys.argv[2]
    s3_folder = sys.argv[3]

    upload_files_to_s3(local_folder, s3_bucket, s3_folder)

