# Idea to crop base layer image around a control point
#(may not work for our purpose/how to incoropaorte?)
#1. load the image and conver to a tensor(will this be issue with tif?)
#2. determine the center of the iamge
#3. calculate the bounds of the ropped region
#4. crop the image tensor using these bounds. 


import torch
import torchvision.transforms as T
from PIL import Image
import matplotlib.pyplot as plt

#load image and convert to a tensor

image_path = 'data/airPort.jpg'
img = Image.open(image_path)
img_tensor = T.ToTensor()(img)

#crop size (height, width)
crop_height, crop_width = 100, 100

#get original image dimensions
_, h, w = img_tensor.shape

#calculate the center position
center_y, center_x = h //2, w // 2

#calculate the bounding box for cropping
y1 = max(0, center_y - crop_height // 2)
y2 = min(h, center_y + crop_height // 2)
x1 = max(0, center_x - crop_width // 2)
x2 = min(w, center_x + crop_width // 2)

#crop 
cropped_tensor = img_tensor[:, y1:y2, x1:x2]

#convert back to PIL for visual
cropped_img = T.ToPILImage()(cropped_tensor)

#display the cropped image
plt.imshow(cropped_img)
plt.axis('off')
plt.show()