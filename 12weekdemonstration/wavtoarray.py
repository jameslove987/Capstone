#Air2Air
#Harrison Boldt

#This code will convert the .wav file made in micpytest into a numpy.ndarray needed to pass into audioprocess

def convertfunc():
	import soundfile as sf
	import subprocess

	subprocess.call(['ffmpeg', '-i', 'test1.mp3', 'convert1.wav'])

	data, fs = sf.read("convert1.wav")


	return data

#data = wavio.read("convert1.wav")

#file_path = "mictest.wav"

#data, fs = wavio.read("mictest.wav")

#frames = wave_read.read

#import scipy as sp

#import wavfile
#import read

#sr, y = sp.wavfile.read("mictest.wav")

#print(y)

#a = read("mictest.wav")

#numpy.array(a[1], dtype=float)


#import numpy as np
#import wavio
#import wave
