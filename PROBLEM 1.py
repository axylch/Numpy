import numpy as np
X = np.random.random((5,5))

xbar = np.mean(X)
sdev = np.std(X)

Z = ((X-xbar)/sdev)

A = np.subtract(X,xbar)
B = np.divide(A,sdev)


print(Z)
print("\nAlter. method:\n",B)

