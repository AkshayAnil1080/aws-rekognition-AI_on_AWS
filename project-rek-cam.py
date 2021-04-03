# webcam photo click
# pip install opencv-python
import cv2

# fucntion -  capability to connect to webcam - 0,1- internal,external webcam
cap = cv2.VideoCapture(1)  #

myphoto ="akshay.jpg"
ret , photo = cap.read()
cv2.imwrite(myphoto,photo)
cap.release()

ret

# upload photo into cloud storage s3 -  need of boto3
region = "ap-south-1"

bucket = "ai-workshop-bucket-akshay"

myphoto

# pip install boto3
import boto3

upimage = "file.jpg"

s3 = boto3.resource('s3')

s3.Bucket(bucket).upload_file(myphoto, upimage)

# rek services to access the photos in s3
rek = boto3.client('rekognition' , region)    #Amazon treat python here as a client

rek.detect_labels(
Image={
          'S3Object': {
              'Bucket': bucket,
              'Name': upimage,
          }
      },
      MaxLabels=10,
      MinConfidence=60
  
)