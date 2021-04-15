

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

cam = cv2.VideoCapture(0)

#set camera resolution
cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640*2)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480*2)
print("Current camera resolution: (" + str(cam.get(3)) + "; " + str(cam.get(4)) + ")")

# create AprilTags detector with options
detector = pupil_apriltags.Detector(families="tag36h11")

frame_number=0

# keep looping
results = 0
while results == 0:

    (grabbed, frame) = cam.read()
    image = rescale(frame, percent=50)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # execute the detector to find the tags (more options exist)
    results = detector.detect(gray, estimate_tag_pose=False, camera_params=None, tag_size=0.17)
    #print("{} AprilTag(s) detected".format(len(results)))

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
