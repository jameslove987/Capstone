# USAGE
# python detect_apriltag_webcam.py

# import the necessary packages
import pupil_apriltags
import cv2
import time

def rescale(frame, percent=60):
    scale_percent = 60
    width = int(frame.shape[1]*scale_percent/100)
    height = int(frame.shape[0]*scale_percent/100)
    dim = (width, height)
    return cv2.resize(frame,dim, interpolation = cv2.INTER_AREA)

# open the webcam
filename = 'CapCal3.mp4'
# load input image and convert to grayscale
print("Loading image...")
<<<<<<< Updated upstream
cam = cv2.VideoCapture(filename)
=======
cam = cv2.VideoCapture(0)
>>>>>>> Stashed changes


#set camera resolution
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640*2)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480*2)
print("Current camera resolution: (" + str(cam.get(3)) + "; " + str(cam.get(4)) + ")")


# create AprilTags detector with options
detector = pupil_apriltags.Detector(families="tag36h11")

frame_number=0
# keep looping
while True:
<<<<<<< Updated upstream
        (grabbed, frame) = cam.read()
        image = rescale(frame, percent=50)

=======
        if not cam.isOpened():
                cam.open(0)
                print('initializing...')
        (grabbed, frame) = cam.read()
        image = rescale(frame, percent=50)
                
>>>>>>> Stashed changes
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # execute the detector to find the tags (more options exist)
        results = detector.detect(gray, estimate_tag_pose=False, camera_params=None, tag_size=0.17)
        #print("{} AprilTag(s) detected".format(len(results)))

        gold = (0, 215, 255)
        cv2.circle(image, (577, 204), 10, gold, 3) #577, 324 (204 for dots)
        # loop over the AprilTag detection results
        for r in results:
                # extract the bounding box (x, y)-coordinates for the AprilTag
                # and convert each of the (x, y)-coordinate pairs to integers
                (ptA, ptB, ptC, ptD) = r.corners
                ptB = (int(ptB[0]), int(ptB[1]))
                ptC = (int(ptC[0]), int(ptC[1]))
                ptD = (int(ptD[0]), int(ptD[1]))
                ptA = (int(ptA[0]), int(ptA[1]))

                # draw the bounding box of the AprilTag detection
                cv2.line(image, ptA, ptB, (0, 0, 255), 2)
                cv2.line(image, ptB, ptC, (0, 0, 255), 2)
                cv2.line(image, ptC, ptD, (0, 0, 255), 2)
                cv2.line(image, ptD, ptA, (0, 0, 255), 2)


                # draw the center (x, y)-coordinates of the AprilTag
                (cX, cY) = (int(r.center[0]), int(r.center[1]))
                cv2.circle(image, (cX, cY), 5, (0, 255, 0), -1)
                # difference in positon
                (diffx, diffy) = (cX-577, cY-204) #577, 184
                (realposx, realposy) = (cX, cY)
                cv2.putText(image, 'Difference in x position: %02.1f' %(diffx), (30, 580), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 0), 2)
                cv2.putText(image, 'Difference in y position: %02.1f' %(diffy), (30, 610), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 0), 2)

                # draw the tag family on the image
                tagFamily = r.tag_family.decode("utf-8")
                tagId = r.tag_id

                cv2.putText(image,str(tagId), (ptA[0], ptA[1] - 15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)
##                print("Found tag in Image: {}".format(frame_number),'with ID ', tagId)

##        # resize the frame, optional
##        image = cv2.resize(image, (0,0), fx=2.0, fy=2.0)
##
#
	# show the frame to our screen and increment the frame
        cv2.imshow("April Tag Detector", image)

        # if the 'q' key is pressed, stop the loop
        key = cv2.waitKey(1) & 0xFF
        if key == 27 or key == ord("q"):
                break
        frame_number=frame_number + 1

# release the camera and close any open windows
cam.release()
cv2.destroyAllWindows()
