#importing boto3 for code
import boto3
#using put object function to upload images to Bucket coursework-bucket-s1311448
#use time.sleep(30) function in order to put a 30second delay between file uploads.
cli = boto3.client('s3')
cli.put_object(Bucket='coursework-bucket-s1311448', Key='/CPDimages/images/image1.jpg')
Sleep(30),
cli = boto3.client('s3')
cli.put_object(Bucket='coursework-bucket-s1311448', Key='/CPDimages/images/image2.jpg')
Sleep(30),
cli = boto3.client('s3')
cli.put_object(Bucket='coursework-bucket-s1311448', Key='/CPDimages/images/image3.jpg')
Sleep(30),
cli = boto3.client('s3')
cli.put_object(Bucket='coursework-bucket-s1311448', Key='/CPDimages/images/image4.jpg')
Sleep(30),
cli = boto3.client('s3')
cli.put_object(Bucket='coursework-bucket-s1311448', Key='/CPDimages/images/image5.jpg')
Sleep(30)