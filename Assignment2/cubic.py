import numpy as np
from scipy.interpolate import CubicSpline
from tqdm import tqdm

def cubic(data, det):
    '''
    Take in the detection file and the original data

    Args:
        if the element in detection file doesn't represent for a click then add it into a new block

        Then apply the new blocks of x and y to the cubic spline

        Use the new funtion to predict unkown values and put it back to the original data

    
    Returns:
        restored data
    '''
    x = np.arange(len(data))
    block = []
    xlabel = []
    pbar1 = tqdm(x)
    pbar2 = tqdm(range(len(det)))
    for i in pbar1:
        pbar1.set_description("Making base data")
        if i not in det:
            block.append(data[i])
            xlabel.append(x[i])
    f = CubicSpline(xlabel, block, bc_type='natural')
    for j in pbar2:
        pbar2.set_description("Calculating Cubic Splines")
        data[det[j]] = f(det)[j]
    return data
