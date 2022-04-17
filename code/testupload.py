import glob
import boto3
import os
import time

BUCKET_NAME = 'coursework-bucket-s1311448'
FOLDER_NAME = 'CPDImages/images/'

s3 = boto3.resource('s3')
jpg_files = glob.glob("CPDImages/images/*.jpg")
png_files = glob.glob("CPDImages/images/*.png")

for filename in jpg_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename,key))
    s3.meta.client.upload_file(filename, BUCKET_NAME, key)
    time.sleep(30)

for filename in png_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename,key))
    s3.meta.client.upload_file(filename, BUCKET_NAME, key)
    time.sleep(30)
    
for filename in txt_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Error file not supported" % (filename,key))
    
#Print Upload complete and inform users only two file types supported.
#For future updates adding a new for function(s) for filetype_files would be added
print("Upload Complete, Please note only .jpg and .png files are supported any others will not be uploaded")