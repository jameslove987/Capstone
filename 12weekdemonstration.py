#Air2AIr
#Love, Boldt 
#updated 7apr21

#Import pyparrot
from pyparrot.Anafi import Anafi

#import for audio
import audiomain
import audioprocess
import micpytest
import wavtoarray

anafi = Anafi(drone_type="Anafi", ip_address="192.168.42.1")
anafi.set_indoor(0)
print("connecting")
success = anafi.connect(10) #Continously attempts to connect to the drone 10 times until the drone is connected
print(success)


#user=input("Give a command: ") #main while loop
a = 1
while a < 5:


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
        while i < 21:
            anafi.move_relative(dx=0,dy=0,dz=0,dradians=.3) #clockwise

            #Video Detection Condition
            cv = 0 # video.videofunc()


            if cv == "forward":
                anafi.fly_direct(0,40,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                anafi.fly_direct(0,-40,0,0,1.9) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                print("Strafing forward")
            elif cv == "backward":
                anafi.fly_direct(0,-40,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                anafi.fly_direct(0,40,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)   
                print("Strafing backward")
            elif cv == "sleft":
                 anafi.fly_direct(-40,0,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                 anafi.fly_direct(40,0,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                 print("Strafing right")
            elif cv == "sright":
                 anafi.fly_direct(40,0,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                 anafi.fly_direct(-40,0,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                 print("Strafing left")
            elif cv == "left":
                anafi.fly_direct(0,0,0,40,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                anafi.fly_direct(0,0,0,-40,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                print("Turning right")
            elif cv == "right":
                anafi.fly_direct(40,0,0,-40,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                anafi.fly_direct(-40,0,0,40,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                print("Turning left")
            elif cv == "up":
                anafi.fly_direct(0,0,0,40,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                anafi.fly_direct(0,0,0,-40,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                print("Ascending")
            elif cv == "down":
                anafi.fly_direct(0,0,0,-40,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                anafi.fly_direct(0,0,0,40,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
                print("Decending") 
                


            i += 1

        print("landing")
        anafi.safe_land(5) #Ensure the mambo lands by sending the command until it shows landed on sensors
    a += 1
         
   
print("DONE - disconnecting")
anafi.disconnect()  #disconnects the drone from the computer

