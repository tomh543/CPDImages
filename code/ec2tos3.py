#importing boto3 for code
import boto3
#import time for delay
import time
#using put object function to upload images to Bucket coursework-bucket-s1311448
#use time.sleep(30) function in order to put a 30second delay between file uploads.
cli = boto3.client('s3')
s3.bucket('coursework-bucket-s1311448').object('images').upload_file('CPDImages/images')
time.sleep(30)
