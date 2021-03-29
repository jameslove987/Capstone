from pyparrot.Anafi import Anafi
anafi = Anafi(drone_type="Anafi", ip_address="192.168.42.1")
anafi.set_indoor(0)
print("connecting")
success = anafi.connect(10) #Continously attempts to 10 times until the drone is connected
print(success)
print("sleeping")
anafi.smart_sleep(5) # Use this which handles packets received while sleeping   Parameters:	timeout – number of seconds to sleep
print("taking off")
anafi.safe_takeoff(5) #Sends commands to takeoff until the mambo reports it is taking off   Parameters:	timeout – quit trying to takeoff if it takes more than timeout seconds
anafi.smart_sleep(1) #delays before movement
print("moving")

user=input("Give a command: ")
while user != "end":
    spin = spininput #input the audio output from Harrisons sybsytem
    cv = cvinput #input the CV ouput from Jerra

    if spin == 1:
        anafi.move_relative(dx=0,dy=0,dz=0,dradians=6.28) #clockwise

    if cv == "forward":
        anafi.fly_direct(0,40,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
        anafi.fly_direct(0,-40,0,0,1.9) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
        print("Strafing forward")
    elif cv == "backward":
        anafi.fly_direct(0,-40,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
        anafi.fly_direct(0,40,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)   
        print("Strafing backward")
    # elif cv == "sleft":
    #     anafi.fly_direct(-40,0,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
    #     anafi.fly_direct(40,0,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
    #     print("Strafing right")
    # elif cv == "sright":
    #     anafi.fly_direct(40,0,0,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
    #     anafi.fly_direct(-40,0,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
    #     print("Strafing left")
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
    else: 
        print("That command is invalid.  Enter a different command.")
    user=input("Give a command: ")


print("landing")
anafi.safe_land(5) #Ensure the mambo lands by sending the command until it shows landed on sensors
print("DONE - disconnecting")
anafi.disconnect()