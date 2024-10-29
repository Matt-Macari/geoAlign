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




#----------------------------------------
        # Draw the matches between the query and train images
    matched_image = cv2.drawMatches(query_image, query_keypoints, train_image, train_keypoints, matches, None, 
                                    flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    

    # Display the image with matches
    cv2.imshow('Matches', matched_image)
    cv2.waitKey(0)  # Wait until a key is pressed
    cv2.destroyAllWindows()  # Close the window 

   # ------------------------------------- 

    # Sort by distance
    sorted_matches = sorted(matches, key=lambda x: x.distance)

    #extract the keypoints
    query_keypoints = np.float32([query_keypoints[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
    train_keypoints = np.float32([train_keypoints[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)

    query_keypoints = query_keypoints.tolist()
    train_keypoints = train_keypoints.tolist()

    # Estimate the transformation matrix
    # You can use cv2.estimateAffine2D, cv2.estimateAffinePartial2D, or cv2.findHomography
    # idk the difference look into this
    # For affine transformation
    #M, mask = cv2.estimateAffine2D(query_keypoints, train_keypoints)  

    # For homography
    # M, mask = cv2.findHomography(query_keypoints, train_pts, cv2.RANSAC)

    #warp the image to fit 
    #aligned_img = cv2.warpAffine(query_image, M, (train_image.shape[1], train_image.shape[0]))

    #draw matches to the final image conatining both images 
    #drawMatches() function does this

    #final_img = cv2.drawMatches(query_image, query_keypoints, train_image, train_keypoints, matches[:50], None)

    #final_img = cv2.resize(final_img,(1000,650))




    #show the final image
    #show matches
    #cv2.imshow("matches:", final_img) 
    #show the aligned image, this does not work as expected right now. 
    #cv2.imshow("aligned image", aligned_img) # show aligned img

    #cv2.waitKey(5000) #set to 0 if you want to exit the picture manually. 
    #cv2.destroyAllWindows()  # This will close the window after the key press.


    #uncommment to print coordinates
    # print("coordinates of query img points: ")
    # for i, pt in enumerate(query_pts):
    #     print(f"keypoint {i + 1}: x = {pt[0][0]}, y = {pt[0][1]}") 

    # print('\n \n \n')

    # print("coordinates of train img points: ")
    # for i, pt in enumerate(train_pts):
    #     print(f"keypoint {i + 1}: x = {pt[0][0]}, y = {pt[0][1]}")  

    """ 
    print("working?")
    for each in matches: 
        print(each.distance) """

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




    # Draw the keypoints on the images
    query_image_with_keypoints = cv2.drawKeypoints(query_image, query_keypoints, None, color=(0, 255, 0), flags=0)
    train_image_with_keypoints = cv2.drawKeypoints(train_image, train_keypoints, None, color=(0, 255, 0), flags=0)

    # Display the images with keypoints




    return width, height, sorted_matches, query_keypoints, train_keypoints


