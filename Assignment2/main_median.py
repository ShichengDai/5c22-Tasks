import unittest
import numpy as np
from scipy.io import wavfile
import matplotlib.pyplot as plt
from checkclick import checkclick
from median import median
from cubic import cubic
import time
from test import median_test


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

MSE1 = np.square(restored1 - GT).mean()
#write restored signal
samplerate = sr
wavfile.write("restored1.wav", samplerate, restored1.astype(np.int16))
#record end time
end1 = time.time()
time1 = end1 - start1

print('\r\n')
print(time1)

print(MSE1)

print('Done')



# test for median
restored1_test = median_test(det,windowsize,y)

class test(unittest.TestCase):
    

    
    def test_case1(self):
        a = restored1
        b = restored1_test
        self.assertEqual(a.all(), b.all(), msg = 'checking the median function')


        
        
if __name__ == '__main__':
    unittest.main()

