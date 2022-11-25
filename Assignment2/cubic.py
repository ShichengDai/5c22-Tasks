import numpy as np
from scipy.interpolate import CubicSpline
from tqdm import tqdm

def cubic(data, det):
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
