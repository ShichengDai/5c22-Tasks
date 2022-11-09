import numpy as np
from MSE import MSECal
dataPR = np.random.randint(1, 10, 20)
dataGT = np.random.randint(1, 10, 20)
MSE = MSECal(dataGT, dataPR)
print(MSE)