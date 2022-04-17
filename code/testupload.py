import glob
import boto3
import os

BUCKET_NAME = 'coursework-bucket-s1311448'
FOLDER_NAME = 'CPDImages/images/'

session = boto3.Session(profile_name='default')
s3 = session.client('s3')

jpg_files = glob.glob("CPDImages/images/*.jpg")
png_files = glob.glob("CPDImages/images/*.jpg.png")

for filename in jpg_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename,key))
    s3.upload_file(filename, BUCKET_NAME, key)

for filename in png_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename,key))
    s3.upload_file(filename, BUCKET_NAME, key)

print("All_Done")