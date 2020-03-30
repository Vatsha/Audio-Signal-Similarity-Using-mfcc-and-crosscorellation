import scipy.fftpack as fft
import scipy.io.wavfile as wav
import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import get_window
import math
import os


def cosine_similar(v1,v2):
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx +=x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)

files = os.listdir("/home/abhijeet/abhi")
#print(files)
(sample_rate2,audio2) = wav.read("apple.wav")
count=0

for i in files:
	try:
		(sample_rate1,audio1) = wav.read("/home/abhijeet/abhi/"+i)
		print(i)
		#print("Time Duration : ",audio1.size/float(sample_rate1))

		#print(audio1.shape)
		if audio1.shape[0] < audio2.shape[0]:
	 		th = cosine_similar(audio1,audio2[0:audio1.shape[0]])
		else:
	 		th = cosine_similar(audio1[0:audio2.shape[0]],audio2)
		count+=1
		#print(count)
		print(th)

	except Exception:
		pass


