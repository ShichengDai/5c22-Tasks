import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from checkclick import checkclick
from median import median



#read files from previous work first
sr, detection = wavfile.read('detectionfile.wav')
sr, y = wavfile.read('degraded.wav')
sr, GT = wavfile.read('myclean.wav')
GT = [data[0] for data in GT ]
##Calculate for median filter


#change window size here
#windowsize = 2n + 2ex + 1  (ex > 1)
ex1 = list(range(1, 100))
ex2 = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000, 2000, 3000, 4000, 5000]
ex = ex1 + ex2

MSE = []
for i in ex:

    det, windowsize = checkclick(detection, i)
    restored1 = median(det,windowsize,y)
    MSE.append(np.square(restored1 - GT).mean())

plt.plot(ex, MSE)
plt.title('Relationship between window size and MSE')
plt.xlabel('K for Window size = 2N + 2K + 1')
plt.ylabel('MSE')
plt.show()















