
import numpy as np


def checkclick(detection):
    det = sorted(np.where(detection == 1)[0])
    s = []
    windowsize = []
    counter = 1
    j = 1
    for i in det:
        s.append(i)
        if i + 1 not in det:
            if len(s) >= 1:
                if counter <= len(s):
                    counter = len(s)
                    while j <= counter:
                        j = j + 1
                        windowsize.append(2 * counter + 3)
                    counter = 1
                    s = []
                    j = 1
    return det, windowsize
