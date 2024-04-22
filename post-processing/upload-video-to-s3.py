import argparse
import boto3
from botocore.exceptions import NoCredentialsError

def upload_video_to_s3(file_name, bucket, folder_path, object_name=None):
    """
    Upload a file to an S3 bucket into a specific folder

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param folder_path: Folder path inside the bucket
    :param object_name: S3 object name. If not specified, file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_name.split('/')[-1]  # Use the base name of the file

    # Full path in bucket as folder_path/object_name
    full_path = f"{folder_path.rstrip('/')}/{object_name}"

    # Create an S3 client
    s3_client = boto3.client('s3')

    try:
        # Upload the file
        response = s3_client.upload_file(file_name, bucket, full_path)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False

def main():
    parser = argparse.ArgumentParser(description="Upload a video to AWS S3")
    parser.add_argument('file_name', type=str, help='Path to the video file to upload')
    parser.add_argument('bucket', type=str, help='Name of the S3 bucket')
    parser.add_argument('folder_path', type=str, help='Folder path inside the bucket')
    parser.add_argument('--object_name', type=str, default=None, help='Object name in the S3 bucket (optional)')

    args = parser.parse_args()

    # Call the upload function
    upload_video_to_s3(args.file_name, args.bucket, args.folder_path, args.object_name)

if __name__ == "__main__":
    main()

