import math
import numpy as np
x=math.log(math.factorial(10**6))
y=math.log(math.sqrt(2*np.pi*(10**6))) + 10**6 *(math.log(10**6)-math.log(np.e))
print (x)
print(y)