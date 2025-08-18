import numpy as np
# a = np.array([[1,5,9,4],[80,2,3,4],[7,8,9,10]])
# print(a[a[0,:].argsort()])
ar = np.array([[0,0,0]])
ar = np.append(ar,[[1,2,3]],axis=0)
ar = np.append(ar,[[31,22,13]],axis=0)
ar = np.append(ar,[[13,112,113],[4,5,6]],axis=0)

print(ar[ar[:,0].argsort()])
