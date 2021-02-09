import numpy as np

def calculate(list):
     array = np.array(list)
     try:
       matrix= array.reshape((3,3))
     except ValueError:
       raise ValueError("List must contain nine numbers.")
     else:
         a=np.reshape(list,(3,3))
         b=[np.mean(matrix,axis=0).tolist(),np.mean(matrix,axis=1).tolist(),np.mean(array).tolist()]
         c=[np.var(matrix,axis=0).tolist(),np.var(matrix,axis=1).tolist(),np.var(array).tolist()]
         d=[np.std(matrix,axis=0).tolist(),np.std(matrix,axis=1).tolist(),np.std(array).tolist()]
         e=[np.max(matrix,axis=0).tolist(),np.max(matrix,axis=1).tolist(),np.max(array).tolist()]
         f=[np.min(matrix,axis=0).tolist(),np.min(matrix,axis=1).tolist(),np.min(array).tolist()]
         g=[np.sum(matrix,axis=0).tolist(),np.sum(matrix,axis=1).tolist(),np.sum(array).tolist()]
         calculations={  'mean': b,'variance': c,'standard deviation': d,'max': e,'min': f,'sum': g }
         return calculations
print(calculate([2,6,2,8,4,0,1,5,7]))
