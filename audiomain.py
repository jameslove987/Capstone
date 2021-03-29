#Air2Air Audio Main
#updated on 28MAR21
#This will serve as main file to call other functions from.

#import big stuff


def runaudio():
    import os
    import shutil

    #import other scripts
    import audioprocess
    import micpytest
    import wavtoarray

    #audio section
    #Use USB mic to create and record audio file .mp3
    micpytest.createwav()

    #Convert data from .mp3 to .wav then return numpy array
    data = wavtoarray.convertfunc()

    #input microphone data to audioprocessing function
    detectresult = audioprocess.audiofunc(data)

    #understand return and do or don't take action
    print (detectresult)

    return detectresult

    # delete.wav file for space.
    os.remove("test1.mp3")
    os.remove("convert1.wav")


        #delete.wav file for space.
    #End of loop







