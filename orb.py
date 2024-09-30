import numpy as np
import cv2  

curr_train_img = 'airportCrop.png'
curr_query_img = 'airPort.jpg'

query_img = cv2.imread(curr_query_img)
train_img = cv2.imread(curr_train_img)




query_img_bw = cv2.cvtColor(query_img,cv2.COLOR_BGR2GRAY)
train_img_bw = cv2.cvtColor(train_img,cv2.COLOR_BGR2GRAY)

#initizialize the ORB detector
orb = cv2.ORB_create()

#detect keypoints and compute the descriptors for the q image and t image
queryKeypoints, queryDescriptors = orb.detectAndCompute(query_img_bw, None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(train_img_bw, None)

# initialize the matcher for matching the keypoints then match them
matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
matches = matcher.match(queryDescriptors, trainDescriptors)
matches = sorted(matches, key=lambda x: x.distance)

#extract the keypoints
query_pts = np.float32([queryKeypoints[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
train_pts = np.float32([trainKeypoints[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

# Estimate the transformation matrix
# You can use cv2.estimateAffine2D, cv2.estimateAffinePartial2D, or cv2.findHomography
# idk the difference look into this
# For affine transformation
M, mask = cv2.estimateAffine2D(query_pts, train_pts)  

# For homography
# M, mask = cv2.findHomography(query_pts, train_pts, cv2.RANSAC)

#warp the image to fit 
#aligned_img = cv2.warpAffine(query_img, M, (train_img.shape[1], train_img.shape[0]))

#draw matches to the final image conatining both images 
#drawMatches() function does this
final_img = cv2.drawMatches(query_img, queryKeypoints, train_img, trainKeypoints, matches[:30], None)

final_img = cv2.resize(final_img,(1000,650))








#show the final image
#cv2.imshow("matches:", final_img) #show matches
#cv2.imshow("aligned image", aligned_img) # show aligned img


""" print("coordinates of query img points: ")
for i, pt in enumerate(query_pts):
    print(f"keypoint {i + 1}: x = {pt[0][0]}, y = {pt[0][1]}") 

print('\n \n \n')

print("coordinates of train img points: ")
for i, pt in enumerate(train_pts):
    print(f"keypoint {i + 1}: x = {pt[0][0]}, y = {pt[0][1]}")  """
""" 
print("working?")
for each in matches: 
    print(each.distance) """

# Get image dimensions
height, width, channels = train_img.shape  # Channels will be 3 for a color image (BGR)
print(f'Image Dimensions: {width}x{height}')

