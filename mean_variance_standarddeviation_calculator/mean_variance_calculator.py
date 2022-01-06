import numpy as np

def calculate(list):

  #Check if list has the right size
  try:
    arr = np.array(list)
    arr = arr.reshape((3,3))
  except:
    raise ValueError("List must contain nine numbers.")

  #Creating dictionary
  calculations = dict.fromkeys(["mean", "variance", "standard deviation", "max", "min", "sum"])

  #Creating Lists for calculations
  meanCollum = []
  meanRow = []
  varianceCollum = []
  varianceRow = []
  stdCollum = []
  stdRow = []
  maxCollum = []
  maxRow = []
  minCollum = []
  minRow = []
  sumCollum = []
  sumRow = []

  #Calculate values
  for i in range(arr.shape[0]):
    collum = arr[: ,i]
    row = arr[i]
    meanCollum.append(collum.mean())
    meanRow.append(row.mean())
    varianceCollum.append(np.var(collum))
    varianceRow.append(np.var(row))
    stdCollum.append(np.std(collum))
    stdRow.append(np.std(row))
    maxCollum.append(np.max(collum))
    maxRow.append(np.max(row))
    minCollum.append(np.min(collum))
    minRow.append(np.min(row))
    sumCollum.append(np.sum(collum))
    sumRow.append(np.sum(row))

  #add values to dictionary
  calculations["mean"] = [meanCollum, meanRow, np.mean(arr)]
  calculations["variance"] = [varianceCollum, varianceRow, np.var(arr)]
  calculations["standard deviation"] = [stdCollum, stdRow, np.std(arr)]
  calculations["max"] = [maxCollum, maxRow, np.max(arr)]
  calculations["min"] = [minCollum, minRow, np.min(arr)]
  calculations["sum"] = [sumCollum, sumRow, np.sum(arr)]


  return calculations
