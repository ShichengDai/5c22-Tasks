def Oddsum(Num):
  oddarr = [0 for k in range(Num)]
  for i in range(Num): 
      oddarr[i] = 2 * i + 1
  Sumcal = sum(oddarr)
  return(Sumcal)

    