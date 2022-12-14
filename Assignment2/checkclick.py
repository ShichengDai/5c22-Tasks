from tqdm import tqdm
import numpy as np


def checkclick(detection, ex):
    '''
    Take in the detection file, variable for window size

    Args:
        Detect the number of consecutive clicks for each click
        Then use the number to make a specific window size for each click
    
    Returns:
        detection file
        window size
    '''
    det = sorted(np.where(detection == 1)[0])
    s = []
    windowsize = []
    counter = 1
    j = 1
    pbar = tqdm(det)
    for i in pbar:
        pbar.set_description("Detecting Clicks")
        s.append(i)
        if i + 1 not in det:
            if len(s) >= 1:
                if counter <= len(s):
                    counter = len(s)
                    while j <= counter:
                        j = j + 1
                        windowsize.append(2 * counter + 2 * ex + 1)
                    counter = 1
                    s = []
                    j = 1
    return det, windowsize
