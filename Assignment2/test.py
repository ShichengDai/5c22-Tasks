import unittest
import numpy as np
from tqdm import tqdm


def median_test(det, windowsize, data):

    #check if windowsie is odd
    pbar = tqdm(range(len(det)))
    for i in pbar:
        pbar.set_description("Processing signals")
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

            data[det[i]] = np.median(block)
            block = []
    restored = data
    return restored



