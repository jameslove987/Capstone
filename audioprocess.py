

def audiofunc(inputdata):
    #MAIN
    # Air to Air Combat Drone MAIN
    # This function will when given data compute a fourier transform of data vector and .

    import struct
    import matplotlib.pyplot as plt
    import numpy as np
    import scipy.io

    #Imports data vector from matlab vector file. Unable to load in .wav file due to file corruption
    #and not updated external packages for python 3.9
    
    ##vector = scipy.io.loadmat(filepath) #import data file DataList.py
    
    # f = open("DataFile.py")
    # for x in f:
        
    #data = vector['x']
    data = inputdata
    signal_length = len(data)
    fs = 48000.0
  
    #create x axis for audio signal graph
    ts = 1/fs
    t = np.arange(0, signal_length,1)
    t = t*ts

    #plot audio signal
    plt.figure(1)
    plt.plot(t, data)
    plt.title('Audio Signal')
    plt.xlabel('Time (s)')
    plt.ylabel('Signal Amplitude')
    #plt.show()

    #fourier transform
    M = 2 ** 18
    data_k_Dbl_Sided = np.fft.fft(data)
    magnitude = abs(data_k_Dbl_Sided)

    #plot of fft without correct x axis
    #plt.figure(2)
    #plt.plot(magnitude)
    #plt.title('Double Sided FFT')
    #plt.ylabel('Frequency Amplitude')

    data_k_Single_sided = data_k_Dbl_Sided[:(len(data_k_Dbl_Sided)//2)]
    magX_k = abs(data_k_Single_sided)



    DFT_res = fs/signal_length
    f_vect = np.arange(0, (fs/2), DFT_res)
    a = len(f_vect)

    #plot of frequency
    plt.figure(2)
    plt.plot(f_vect, magX_k)
    plt.xlabel('Frequency Hz')
    plt.ylabel('Signal Amplitude')
    plt.title('Frequency of Signal')
    plt.ylabel('Frequency Amplitude')
    plt.xlim([150, 1000])
    plt.ylim([0, 1000])


    #Detection Algorithm configured for plane
    #detection_vectHz = f_vect[150:250]
    #detection_vectMag = magX_k[150:250]
    
    peakcount = 0
    
    #print(np.mean(magX_k[150:1000]))
    
    classdata = magX_k[1:1000]
    
    for i in range(0, len(classdata)):
        if classdata[i] > 200:
            peakcount = peakcount+1
    
    #print((detection_vectHz))
    #print((detection_vectMag))
    print("peak count")
    print(peakcount)  
    
    if peakcount >= 5:
        detect = 1
    else:
        detect = 0
        
    if detect == 1:
        print("Drone Detected")
    else: 
        print("Drone Not Detected")


    #plt.show()
    return detect





