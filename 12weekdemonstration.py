#Air2AIr
#Love, Boldt 
<<<<<<< HEAD
#updated 20apr21
=======
#updated 14apr21
#Hopper 38 at 1125
#Dawkins is in charge of room Record by Monday
>>>>>>> origin

#Import pyparrot
from pyparrot.Anafi import Anafi

#import for audio
import audiomain
import audioprocess
import micpytest
import wavtoarray

#import cv
import pupil_apriltags
import cv2
import time
import Vision


anafi = Anafi(drone_type="Anafi", ip_address="192.168.42.1")
anafi.set_indoor(0)
print("connecting")
#7C45ASBXW8BL
success = anafi.connect(10) #Continously attempts to connect to the drone 10 times until the drone is connected
print(success)

#turn camera on
rtsp_url = "rtsp://192.168.42.1/live"
cam = cv2.VideoCapture(rtsp_url)
if not cam.isOpened():
    cam.open(rtsp_url)
    print('initializing camera...')


#user=input("Give a command: ") #main while loop
a = 1
while a < 3:


    spin = audiomain.runaudio(); #input the audio output from Harrisons sybsytem
    print(spin)    

    #audio response protocol
    if spin == 1:
       
        #take off
        print("sleeping")
        anafi.smart_sleep(5) # Use this which handles packets received while sleeping   Parameters:	timeout – number of seconds to sleep
        print("taking off")
        anafi.safe_takeoff(5) #Sends commands to takeoff until the mambo reports it is taking off   Parameters:	timeout – quit trying to takeoff if it takes more than timeout seconds
        anafi.smart_sleep(1) #delays before movement
        print("moving")

       #spin code the loop runtime and radians are configureable to adjust spin speed.
        i = 1
        while i < 9:
            anafi.move_relative(dx=0,dy=0,dz=0,dradians=.7) #clockwise
            
            #initializations 
            #count for later
            count = 0 
<<<<<<< HEAD
            #JAY/JERRA camera input into script
            gray, image = Vision.getnewframe(cam)
            
            #JAY/JERRA ATD = April Tag detected? function
            ATD = Vision.is_april(gray)
            
            if ATD == 1:
                print("found APRIL TAG******")
                coord = Vision.get_xy(gray, image)
                x_vector = int(coord.get('x',0))
                y_vector = int(coord.get('y',0))
                print(x_vector)
                print(y_vector)
                
                #x_vector = 50 #initialize x vector
                while (x_vector > 10) or (x_vector < -10): 
                    #JAY/JERRA x_vector = apriltag x vector function
                    (x_vector, y_vector) = Vision.get_xy(gray, image)
                    
                    #move anafi left or right depending on x
                    #move right
                    if x_vector > 10:
                        #clockwise
                        anafi.move_relative(dx=0,dy=0,dz=0,dradians=.1) 
                            
                            
                    #move left
                    if x_vector < -10:
                        #COUNTER clockwise
                        anafi.move_relative(dx=0,dy=0,dz=0,dradians=-.1) 
=======
            #JAY/JERRA camera input into script 
            
            #JAY/JERRA ATD = April Tag detected? function may need multiple of these for redundancies 
            if ATD == 1:
            
                #x_vector = 50 #initialize x vector
                while (x_vector > 10) or (x_vector < -10): 
                    #JAY/JERRA x_vector = apriltag x vector function
                    
                    #move anafi left or right depending on x
                    #move right
                        if x_vector > 10:
                            #clockwise
                            anafi.move_relative(dx=0,dy=0,dz=0,dradians=.1) 
                            
                            
                    #move left
                        if x_vector < -10:
                           #COUNTER clockwise
                           anafi.move_relative(dx=0,dy=0,dz=0,dradians=-.1) 
>>>>>>> origin
                          
                    
                    
                #y_vector = 50 #initialize y vector
                while (y_vector > 10) or (y_vector < -10): 
                    #JAY/JERRA y_vector = apriltag y vector function
<<<<<<< HEAD
                    (x_vector, y_vector) = Vision.get_xy(gray, image)
                    
                    #move anafi up or down depending on y
                    #move up
                    if y_vector > 10:
                        anafi.fly_direct(0,0,0,5,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                            
                    #move down
                    if y_vector < -10:
                        anafi.fly_direct(0,0,0,-5,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                
                #moving to target                        
                while (ATD != 0) :
                    #move forward function
                    anafi.fly_direct(0,40,0,0,.5) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                    #april tag detection function
                    (gray, image) = Vision.getnewframe(cam)
                    ATD = Vision.is_april(gray)
=======
                    #move anafi up or down depending on y
                    #move up
                        if y_vector > 10:
                             anafi.fly_direct(0,0,0,5,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                            
                    #move down
                        if y_vector < -10:
                           anafi.fly_direct(0,0,0,-5,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                                        
                while (ATD != 0) :
                    #JAMES move forward function
                    anafi.fly_direct(0,40,0,0,.5) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                    #JERRA / JAY april tag detection function
>>>>>>> origin
                    
                    #count loop number for return
                    count += 1
                    
            #Drone moves back number of interations of count
            count2 = 0 
            while (count2 != count):
<<<<<<< HEAD
                #move drone backward
=======
                #JAMES move drone backward
>>>>>>> origin
                anafi.fly_direct(0,-40,0,0,.5) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                count2 += 1
            
            #finish the spin loop 
            
            
            ###################
            #Notes
            ###################    
            #Pass data in form .mp4 or webcam
            #Video Detection Condition
            #cv = 0 # video.videofunc()


<<<<<<< HEAD
            #if import pupil_apriltags cv == "forward":
=======
            #if cv == "forward":
>>>>>>> origin
            #    anafi.fly_direct(0,40,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    anafi.fly_direct(0,-40,0,0,1.9) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    print("Strafing forward")
            #elif cv == "backward":
            #    anafi.fly_direct(0,-40,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    anafi.fly_direct(0,40,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)   
            #    print("Strafing backward")
            #elif cv == "sleft":
            #     anafi.fly_direct(-40,0,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #     anafi.fly_direct(40,0,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #     print("Strafing right")
            #elif cv == "sright":
            #     anafi.fly_direct(40,0,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #     anafi.fly_direct(-40,0,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #     print("Strafing left")
            #elif cv == "left":
            #    anafi.fly_direct(0,0,0,40,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    anafi.fly_direct(0,0,0,-40,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    print("Turning right")
            #elif cv == "right":
            #    anafi.fly_direct(40,0,0,-40,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    anafi.fly_direct(-40,0,0,40,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    print("Turning left")
            #elif cv == "up":
            #    anafi.fly_direct(0,0,0,40,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    anafi.fly_direct(0,0,0,-40,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    print("Ascending")
            #elif cv == "down":
            #    anafi.fly_direct(0,0,0,-40,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    anafi.fly_direct(0,0,0,40,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
            #    print("Decending") 
                


            i += 1

        print("landing")
        anafi.safe_land(5) #Ensure the mambo lands by sending the command until it shows landed on sensors
    a += 1
         
   
print("DONE - disconnecting")
anafi.disconnect()  #disconnects the drone from the computer

#everything is prerecorded.


