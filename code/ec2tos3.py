#import glob for searching file types
#import os for filepaths
#import time to set delays
#import boto3 to run python
import glob
import boto3
import os
import time

BUCKET_NAME = 'coursework-bucket-s1311448'
FOLDER_NAME = 'CPDImages/images/'

s3 = boto3.resource('s3')
jpg_files = glob.glob("CPDImages/images/*.jpg")
png_files = glob.glob("CPDImages/images/*.png")
#for future updates addition of new file formats would be done by adding e.g. gif_files = glob.glob(""CPDImages/images/*.")

#checks for jpg files and uploads with a timer delay of 30 seconds between each upload
for filename in jpg_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename,key))
    s3.meta.client.upload_file(filename, BUCKET_NAME, key)
    time.sleep(30)
    
#checks for png files and uploads with a timer delay of 30 seconds between each upload
for filename in png_files:
    key = "%s/%s" % (FOLDER_NAME, os.path.basename(filename))
    print("Putting %s as %s" % (filename,key))
    s3.meta.client.upload_file(filename, BUCKET_NAME, key)
    time.sleep(30)
#For future updates adding a new for function(s) for filetype_files would be added 
#Check to see if any files are not jpg or png. If file exists notify user.  
if filename != jpg_files or filename != png_files:
    print ("File not in correct format png & jpg only")
    
    
#Print Upload complete and inform users only two file types supported.
print("Upload Complete, Please note only .jpg and .png files are supported any othell not be uploaded")