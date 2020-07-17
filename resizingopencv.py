#Code for resizing images using OpenCV. 
#OpenCV is a better choice for resizing images as it keeps the exif data of the image in account. 
#Resizing a large image would significantly accelerate the performance of the process.


import cv2,os

path = '/content/images/'
dirs = os.listdir(path)
i = 0

for im in dirs:

  oriimg = cv2.imread(path+im,cv2.IMREAD_COLOR)
  h, w, depth = oriimg.shape
  w1 = 500
  h1 = int(500*(h/w))
  new_img = cv2.resize(oriimg,(w1,h1))
  new_name = str(i)+ 'resized.jpeg'
  cv2.imwrite('/content/resized_images/'+new_name,new_img)
  i = i+1