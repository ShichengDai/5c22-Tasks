import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from cubic import cubic
import time
from checkclick import checkclick
from playsound import playsound

#read files from previous work first
sr, detection = wavfile.read('detectionfile.wav')
sr, y = wavfile.read('degraded.wav')
sr, GT = wavfile.read('myclean.wav')
GT = [data[0] for data in GT ]
samplerate = sr




##calculate for cubicspline

start2 = time.time()
det, windowsize = checkclick(detection, 1)
restored2 = cubic(y, det)
MSE2 = np.square(restored2 - GT).mean()
end2 = time.time()
time2 = end2 - start2
wavfile.write("restored2.wav", samplerate, restored2.astype(np.int16))
playsound('restored2.wav')
plt.figure()
plt.subplot(211)
plt.plot(GT)
plt.title('Ground Truth')
plt.xlabel('Frequecy')
plt.ylabel('Magnitude')
plt.subplots_adjust(hspace=0.5)
plt.subplot(212)
plt.plot(restored2)
plt.title('Restored signal using cubic spline')
plt.xlabel('Frequecy')
plt.ylabel('Magnitude')
plt.show()