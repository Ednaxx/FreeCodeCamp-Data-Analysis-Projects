import numpy as np

def calculate(list):

  if (len(list) < 9):
    raise ValueError("List must contain nine numbers.")

  matrix = np.array(list).reshape((3,3))

  # axis1 = columns, axis2 = rows

  calculations = {
    'mean': [matrix.mean(0).tolist(), matrix.mean(1).tolist(), matrix.mean().tolist()],
    'variance': [matrix.var(0).tolist(), matrix.var(1).tolist(), matrix.var().tolist()],
    'standard deviation': [matrix.std(0).tolist(), matrix.std(1).tolist(), matrix.std().tolist()],
    'max': [matrix.max(0).tolist(), matrix.max(1).tolist(), matrix.max().tolist()],
    'min': [matrix.min(0).tolist(), matrix.min(1).tolist(), matrix.min().tolist()],
    'sum': [matrix.sum(0).tolist(), matrix.sum(1).tolist(), matrix.sum().tolist()]
  }
  
  return calculations
  