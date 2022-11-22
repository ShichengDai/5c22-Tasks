import numpy as np
data = [1, 3, 5, 10, 5, 4, 2, 6, 30, 30, 50, 5, 4, 7, 6, 1, 2, 3, 60]
N = len(data)
  ## Find the clicks
  # Make a threshold
data_count_mean = np.mean(data)
diff_mean = np.mean(data - data_count_mean)
thres = data_count_mean + diff_mean
  # Find clicks
pos = np.where(data > thres)
pos = pos[0]
  # Find the number of continious clicks as counter
s = []
counter = 1
for i in sorted(set(pos)):
    s.append(i)
    if i + 1 not in pos:
        if len(s) >= 1:
          if counter <= len(s):
              counter = len(s)
              s = []
  # Define window size
window_size = 2 * counter + 3
#check if window_size is odd
if window_size % 2 == 1:
  # New data should have a length of original length + window_size - 1
    pad = (1, counter + 1)
    pad = np.zeros(pad)[0]
    # For the size of data to 1 * n
    data = np.array(data).reshape(1, -1)[0]
    pad_data = np.hstack((pad, data, pad))
    # calculate median in a period of data and put it into the data
    s = []
    for j in range(len(data)):
        s = pad_data[j : j + window_size]
        s = np.sort(s)
        data[j] = s[counter + 1]
        pad_data[j + counter + 1] = data[j]
        s = []
print(data)
print(pad_data)