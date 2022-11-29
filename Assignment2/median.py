import numpy as np
from tqdm import tqdm


def median(det, windowsize, data):
    '''
    Take in the detection file, window size for each click and the original data

    Args:
        if the length of data is enough then append nothing to the dataset
        if the length of data is not enough for window then append zeros to the array according to different situations
        Args:
             if no enough space for the left half then add zeros to the left
             if no enough space for the right half then add zeros to the right
    
    Returns:
        restored data
    '''
    pbar = tqdm(range(len(det)))
    # compute the median for each click
    for i in pbar:
        pbar.set_description("Processing signals")
        
        #check if windowsie is odd
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
            data[det[i]] = blocksort[padsize]
            block = []
    restored = data
    return restored
