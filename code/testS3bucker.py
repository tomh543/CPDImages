    # Create bucket
    try:
        if region is 'us-east-1":
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket='testbettercode')
        else:
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name,
                                    CreateBucketConfiguration=location)
    except ClientError as e:
        logging.error(e)
        return False
    return True