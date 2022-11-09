import numpy as np 

def MSECal(dataGT, dataPR):
  err = np.square(dataGT-dataPR).mean()
  return err