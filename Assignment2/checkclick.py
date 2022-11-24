# in this function, the location of clicks should be detected and returned to the main function.
# blocksize should be used to set thresholds for each block to make sure that the clicks are clicks in that period of signal
# contain three parts here 
# 1. segment split data into several blocks 
# 2. check clicks in difeerent blocks 
# 3. combine the subsignals into a whole one.
import numpy as np


def segment(data, blocksize):
  
  # split the data into first n parts with size of blocksize
  # set the remaining datas into data_remain which will be detected at last

  n = int(len(data) / blocksize) 
  data_new = data[: n * blocksize]
  data_seg = np.array_split(data_new, n)
  data_remain = data[len(data) - 1 - (len(data) % blocksize) - 1: len(data) - 1]
  
  # check clicks in the first n blocks

  for i in range(n):
    # Make a threshold
    data_count_mean = np.mean(data_seg[i])
    diff_mean = np.mean(data_seg[i] - data_count_mean)
    thres = data_count_mean + diff_mean
    # Find clicks
    pos = np.where(data_seg[i] > thres)
    pos = pos[0]
  return subdata
