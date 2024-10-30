import numpy as np
import cv2  


def orb_detect(train_image, query_image):


    query_image = cv2.imread(query_image)
    train_image = cv2.imread(train_image)


    query_image_bw = cv2.cvtColor(query_image,cv2.COLOR_BGR2GRAY)
    train_image_bw = cv2.cvtColor(train_image,cv2.COLOR_BGR2GRAY)

    #initizialize the ORB detector
    orb = cv2.ORB_create()

    
    #detect keypoints and compute the descriptors for the q image and b image
    query_keypoints, query_descriptors = orb.detectAndCompute(query_image_bw, None)
    train_keypoints, train_descriptors = orb.detectAndCompute(train_image_bw, None)


    # initialize the matcher for matching the keypoints then match them
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = matcher.match(query_descriptors, train_descriptors)

    # Sort by distance
    sorted_matches = sorted(matches, key=lambda x: x.distance)



#---------SHOW MATCHES VISUAL: ---------------------------------------------------------
#---------------------------------------------------------------------------------------
    # Draw the matches between the query and train images
    matched_image = cv2.drawMatches(query_image, query_keypoints, train_image, train_keypoints, sorted_matches, None, 
                                    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    
    # Display the image with matches
    cv2.imshow('Matches', matched_image)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()  # Close the window 
#--------------------------------------------------------------------------------------- 
#--------------------------------------------------------------------------------------- 

    #extract the keypoints
    query_keypoints = np.float32([query_keypoints[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    train_keypoints = np.float32([train_keypoints[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    query_keypoints = query_keypoints.tolist()
    train_keypoints = train_keypoints.tolist()

    #uncommment to print coordinates
    # print("coordinates of query img points: ")
    # for i, pt in enumerate(query_pts):
    #     print(f"keypoint {i + 1}: x = {pt[0][0]}, y = {pt[0][1]}") 

    # print('\n \n \n')

    # print("coordinates of train img points: ")
    # for i, pt in enumerate(train_pts):
    #     print(f"keypoint {i + 1}: x = {pt[0][0]}, y = {pt[0][1]}")  


    #uncomment to show dimensions
    # Get image dimensions
    height, width, channels = train_image.shape  # Channels will be 3 for a color image (BGR)
    #print(f'Image Dimensions: {width}x{height}')


    # uncommment to print coordinates
    """     print("coordinates of query img points: ")
    for i, pt in enumerate(query_keypoints):
        print(f"keypoint {i + 1}: x = {pt[0][0]}, y = {pt[0][1]}") 

    print('\n \n \n')

    print("coordinates of train img points: ")
    for i, pt in enumerate(train_keypoints):
        print(f"keypoint {i + 1}: x = {pt[0][0]}, y = {pt[0][1]}")  


    print(f'\n\nsorted_matches ({len(sorted_matches)}): {sorted_matches} \n\n\n')
    print(f'\n\nquery_keypoints ({len(query_keypoints)}): {query_keypoints} \n\n\n')
    print(f'\n\ntrain_keypoints ({len(train_keypoints)}): {train_keypoints} \n\n\n') """


    return width, height, sorted_matches, query_keypoints, train_keypoints


