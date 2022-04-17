def upload_to_s3(df):
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file('CPDImages/images', 'coursework-bucket-s1311448', 'image1.jpg' --recursive)
upload_to_s3()