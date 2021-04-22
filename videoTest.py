import rtsp
import cv2
from Vision import rescale
#mport detect_apriltag_webcam  as daw
#client = rtsp.Client(rtsp_server_uri = 'rtsp://192.168.42.1/live')
#cam = cv2.VideoCapture(client)



#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

rtsp_url = "rtsp://192.168.42.1/live"
cam = cv2.VideoCapture(rtsp_url)
if not cam.isOpened():
    cam.open(rtsp_url)
    print('initializing camera...')
    

while(1):
    print("go time")
    (grabbed, frame) = cam.read()
    print("go time2")
    #image = rescale(frame, percent=50)
    cv2.imshow('VIDEO', frame)
    print("go time3")
    cv2.waitKey(1)
#image = rescale(frame, percent=50)
