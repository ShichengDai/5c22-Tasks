# check if windowsie is odd
import numpy as np
data = [5,4,1,3,0,0,0,0,0,0,0,0,0,0,7,6,9,1,0,2]
det = [0,1,5,17,18]
windowsize = [7,7,5,7,7]
for i in range(len(det)):

    # compute the median for each click
    if windowsize[i] % 2 == 1:

         # check if the length of block is adequete for median filter
        padsize = int((windowsize[i] - 1) / 2)
        block = []

           # situations that length is enough
        if padsize <= det[i] and padsize <= len(data) - det[i] - 1:

            # make a new block to compute for median
            block = data[det[i] - padsize: det[i] + padsize]
            # situations that the left half of median filter is not enough
        elif padsize > det[i] and padsize <= len(data) - det[i] - 1:

            ex = np.zeros(padsize - det[i], int)
            block = np.append(ex, data[0 : windowsize[i] - len(ex)])
            # situations that the right half of median filter is not enough
        elif padsize <= det[i] and padsize > len(data) - det[i] - 1:

            ex = np.zeros(padsize - len(data) + det[i] + 1, int)
            block = np.append(data[det[i] - padsize:], ex)

        blocksort = sorted(block)
        print(data)
        print(windowsize[i])
        print(det[i])
        print(padsize)
        print(ex)
        print(block)
        print(blocksort)
        data[det[i]] = blocksort[padsize]
        print(data)
        block = []
