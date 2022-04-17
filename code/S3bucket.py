#import of boto3 in order to run the python code
import boto3
#import of logging & ClientError in order to allow for error testing
import logging
from botocore.exceptions import ClientError

# function to create bucket
def create_bucket(bucket_name, region=None):
#creating the bucket if bucket created it will return True else false, 
#if region is not specified it will default to us-east-1

    
    try:
        if region is None:
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True
#runs create_bucket function for creating "coursework-bucket-s1311448" bucket in region us-east-1
create_bucket("coursework-bucket-s1311448")