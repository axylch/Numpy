import numpy as np
a = np.linspace(1,100,100)
b = np.resize(a,(10,10))
c = b

f = c*b
result = f[f%3 == 0]
print (result)
