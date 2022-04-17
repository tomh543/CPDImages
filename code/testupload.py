import glob
import boto3
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

print("All_Done")