#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  Vision.py
#  
#  Copyright 2021  <pi@raspberrypi>
import cv2
import pupil_apriltags

#  
#  
def is_april(gray):
    results = []
    # execute the detector to find the tags (more options exist)
    detector = pupil_apriltags.Detector(families="tag36h11")

    results = detector.detect(gray, estimate_tag_pose=False, camera_params=None, tag_size=0.17)
    #print(results)
    print("{} AprilTag(s) detected".format(len(results)))
    if results != []:
        go_time  = 1
    else:
        go_time = 0
    return go_time

def get_xy(gray, image):
     # execute the detector to find the tags (more options exist)
        detector = pupil_apriltags.Detector(families="tag36h11")
        results = detector.detect(gray, estimate_tag_pose=False, camera_params=None, tag_size=0.17)
        #print("{} AprilTag(s) detected".format(len(results)))

        gold = (0, 215, 255)
        cv2.circle(image, (577, 204), 10, gold, 3) #577, 324 (204 for dots)
        # loop over the AprilTag detection resultsimage
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
                print(cX, cY)
                cv2.circle(image, (cX, cY), 5, (0, 255, 0), -1)
                # difference in positon
                (diffx, diffy) = (cX-577, cY-204) #577, 184
        
                (realposx, realposy) = (cX, cY)
                
                cv2.putText(image, 'Difference in x position: %02.1f' %(diffx), (30, 580), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 0), 2)
                cv2.putText(image, 'Difference in y position: %02.1f' %(diffy), (30, 610), cv2.FONT_HERSHEY_SIMPLEX,1.0, (0, 255, 0), 2)
                
        
                ##################################################################################
        
            #return {'x': diffx, 'y':diffy}
    # in main script coord = get_xy(gray)
    # coord.get('x',0)
    # coord.get('y',0)
    
def getnewframe(cam):
        (grabbed, frame) = cam.read()
        image = rescale(frame, percent=50)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        return (gray, image)
        
def rescale(frame, percent=60):
    scale_percent = 60
    width = int(frame.shape[1]*scale_percent/100)
    height = int(frame.shape[0]*scale_percent/100)
    dim = (width, height)
    return cv2.resize(frame,dim, interpolation = cv2.INTER_AREA)        

