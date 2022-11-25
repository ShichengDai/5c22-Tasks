import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from checkclick import checkclick
from median import median
from cubic import cubic
import time


#read files from previous work first
sr, detection = wavfile.read('detectionfile.wav')
sr, y = wavfile.read('degraded.wav')
sr, GT = wavfile.read('myclean.wav')
GT = [data[0] for data in GT ]

##Calculate for median filter

#record start time
start1 = time.time()
det, windowsize = checkclick(detection)
restored1 = median(det,windowsize,y)
MSE1 = np.sum((restored1 - GT) ** 2).mean()
#write restored signal
samplerate = sr
wavfile.write("restored1.wav", samplerate, restored1.astype(np.int16))
#record end time
end1 = time.time()
time1 = end1 - start1
print('Done')
print(MSE1)
print(time1)


##calculate for cubicspline
restored2 = cubic(y, det)
MSE2 = np.sum((restored1 - GT) ** 2).mean()
wavfile.write("restored2.wav", samplerate, restored2.astype(np.int16))
print(MSE2)
plt.plot(restored2)
plt.show()
