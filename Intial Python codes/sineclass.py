import matplotlib.pyplot as plt
import numpy as np


#class Sine:
 #   def __init__(self,angle):
  #      self.angle=angle

    #def Show(self):
fig, ax = plt.subplots(1)
x = np.linspace(0, 2 * np.pi, 1001)
y = np.sin(x+np.pi/2)
z = np.sin(x)
ax.plot(x, y,x,z)
plt.xlim(0, 2 * np.pi)
plt.grid(True, which='both')
plt.axhline(y=1, color='g')
plt.axhline(y=0, color='k')
plt.axhline(y=-1, color='r')
ax.set_xticks(np.arange(0, 2 * np.pi + 0.01, np.pi / 4))
plt.ylim([-2, 2])
        # labels = ['$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$',
        # r'$5\pi/4$', r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$']
        # ax.set_xticklabels(labels)
plt.show()
    #def addSine(self):

