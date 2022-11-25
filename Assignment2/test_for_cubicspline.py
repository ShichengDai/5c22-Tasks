import numpy as np
from scipy.interpolate import CubicSpline
data = [5,4,1,3,0,0,0,0,0,0,0,0,0,0,7,6,9,1,0,2]
det = [0,1,5,17,18]
x = np.arange(len(data))
block = []
xlabel = []
for i in x:
    if i not in det:
        block.append(data[i])
        xlabel.append(x[i])
print(block)
print(xlabel)
f = CubicSpline(xlabel, block, bc_type='natural')
print(np.shape(f(det)))
for j in range(len(det)):
    data[det[j]] = f(det)[j]
print(data)

#for j in det:
#    data[j] = np.array(f(j))[0]
#print(data)