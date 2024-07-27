'''
#import matplotlib.animation as animation

#fig = plt.figure()
x = np.arange(0, 2*np.pi,0.01)
y=np.sin(x)
#z = np.cos(x)
#ax2 = fig.add_subplot(122)
plt.xlim([0, 2])

plt.plot(x,y)
plt.grid(True, which='both')
plt.axhline(y=1, color='g')
plt.axhline(y=0, color='k')
plt.axhline(y=-1, color='r')
plt.xlabel('x values from 0 to 4pi')  # string must be enclosed with quotes '  '
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()
'''

import matplotlib.pyplot as plt
import numpy as np

#from matplotlib import rc
#rc('text', usetex=True) # Use LaTeX font

#import seaborn as sns
#sns.set(color_codes=True)
fig, ax = plt.subplots(1)
x = np.linspace(0, 2*np.pi, 1001)
y = np.sin(x)
z=np.cos(x)
ax.plot(x, y,x,z)
plt.xlim(0, 2*np.pi)
plt.grid(True, which='both')
plt.axhline(y=1, color='g')
plt.axhline(y=0, color='k')
plt.axhline(y=-1, color='r')
ax.set_xticks(np.arange(0, 2*np.pi+0.01, np.pi/4))
plt.ylim([-2,2])
#labels = ['$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$',
         # r'$5\pi/4$', r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$']
#ax.set_xticklabels(labels)
plt.show()