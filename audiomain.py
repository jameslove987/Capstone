#Air2Air MAIN 

#This will serve as main file to call other functions from.

#import big stuff
import os
import shutil   

#import other scripts
import audioprocess
import micpytest
import wavtoarray

#audio section

#While Loop start
i = 1
while i < 2:
    
    #Use USB mic to create and record audio file .mp3
    micpytest.createwav()
    print("Check1")
    
    #Convert data from .mp3 to .wav then return numpy array
    data = wavtoarray.convertfunc()
    print("Check2")
    print(data)
    
    #input microphone data to audioprocessing function
    detectresult = audioprocess.audiofunc(data)  
    print("Check3")
    
    #understand return and do or don't take action
    print (detectresult)
    i += 1
    
    

    #delete.wav file for space.
#End of loop







