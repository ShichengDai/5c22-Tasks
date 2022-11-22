import numpy as np
from MSE import MSECal
from OddSum import Oddsum
Num = 5
dataPR = np.random.randint(1, 10, 20)
dataGT = np.random.randint(1, 10, 20)
MSE = MSECal(dataGT, dataPR)
Odd = Oddsum(Num)
print(MSE)
print(Odd)