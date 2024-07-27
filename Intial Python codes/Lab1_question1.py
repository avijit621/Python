import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.special import gamma
import matplotlib.ticker as mticker

x=[i for i in range(1,10**6)]
# for computational ease we use gamma function to plot the value of the factorial
y=[math.log(gamma(i)) for i in x]
z= [math.log(math.sqrt(2*np.pi*i))+i* (math.log(i)-math.log(np.e))for i in x]
fig,ax=plt.subplots(1)
ax.plot(x,z,color='blue',label="Stirling's Approximation")
ax.plot(x,y,color="red",label="Actual value of factorial")
# Rotating the x labels at an angle 45degree to prevent overlapping
for tick in ax.get_xticklabels():
    tick.set_rotation(45)
f = mticker.ScalarFormatter(useOffset=False, useMathText=True)
g = lambda x, pos: "${}$".format(f._formatSciNotation('%0.5e' % x))
# for formatting the x labels and y labels correctly
plt.gca().xaxis.set_major_formatter(mticker.FuncFormatter(g))
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(g))
ax.set_title("Comparing stirling's approximation with original values")
ax.set_xlabel("The integer values")
ax.set_ylabel("Logarithm of the factorial values ")
ax.legend()
plt.show()
