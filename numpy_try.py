import numpy as np
#A=np.array([1,2,3,4])
#print(A)
#print(A+A)
#print(np.sqrt(A))
#M=np.zeros(10)
#print(M)
#M = np.ones((10,10))
#print(M)
A=np.array([[1,2],[3,4]])
Ainv=np.linalg.inv(A)
#print(Ainv)
print(np.diagonal(A))
print(np.trace(A))
B=np.array([2,3])
x=np.linalg.solve(A,B)
print(x)
