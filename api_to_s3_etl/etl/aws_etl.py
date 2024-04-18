import boto3
from configs.info_config import ACCESS_KEY_ID, ACCESS_KEY

def connect_to_s3() -> boto3.s3:
    '''
    Create an S3 Client Instance using Boto3

    :return: S3 Client that will be used to upload files to an S3 Bucket
    '''
    try:
        s3 = boto3.client('s3',
                          aws_access_key_id=ACCESS_KEY_ID,
                          aws_secret_access_key=ACCESS_KEY)
        return s3
    
    except Exception as e:
        print(e)

def upload_file(s3: boto3.s3, file_path: str, bucket: str, file_name: str) -> None:
    '''
    Upload file to S3 Bucket.

    :param `s3`: S3 Client reference.
    :param `file_path`: Path of the saved Modified CSV Data.
    :param `bucket`: Name of the bucket in S3.
    :param `file_name`: Saved file name in the file path.
    '''
    try:
        s3.upload_file(file_path, bucket, f"games/{file_name}")
        print('File uploaded.')

    except Exception as e:
        print(e)