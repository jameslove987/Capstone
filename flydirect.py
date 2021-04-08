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

anafi.fly_direct(0,0,90,0,2) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
#anafi.fly_direct(0,0,0,0,1) #fly_direct(roll, pitch, yaw, vertical_movement, duration)
print("Decending")

print("landing")
anafi.safe_land(5) #Ensure the mambo lands by sending the command until it shows landed on sensors
print("DONE - disconnecting")
anafi.disconnect()