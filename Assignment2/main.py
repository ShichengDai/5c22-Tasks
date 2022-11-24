import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from checkclick import checkclick
from median import median

#read files from previous work first
sr, detection = wavfile.read('detectionfile.wav')
sr, data = wavfile.read('degraded.wav')
sr, GTdata = wavfile.read('myclean.wav')

det, windowsize = checkclick(detection)
restored = median(det,windowsize,data)
plt.plot(data)
plt.show()
