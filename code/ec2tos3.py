#importing boto3 for code
import boto3
#import time for delay
import time
#using put object function to upload images to Bucket coursework-bucket-s1311448
#use time.sleep(30) function in order to put a 30second delay between file uploads.
s3 = boto3.resource('s3')
s3.meta.client.upload_file('CPDImages/images/image1.jpg', 'coursework-bucket-s1311448', 'image1.jpg')