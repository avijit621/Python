import matplotlib.pyplot as plt
import numpy as np


class Sine:
    def __init__(self, angle):
        self.angle = angle
        self.x=0
        self.y=0
        self.z =0

    def addsine(self,add_angle):
        self.add_angle= self.angle
        self.x = np.linspace(0, 2 * np.pi, 1001)
        self.y = np.sin(self.x + (np.pi/180)*(self.angle))
        self.z = np.sin(self.x)


    def show(self):
        fig, ax = plt.subplots(1)
        x = np.linspace(0, 2 * np.pi, 1001)
        y = np.sin(x + np.pi / 2)
        z = np.sin(x)
        ax.plot(x, y, x, z)
        plt.xlim(0, 2 * np.pi)
        plt.grid(True, which='both')
        plt.axhline(y=1, color='g')
        plt.axhline(y=0, color='k')
        plt.axhline(y=-1, color='r')
        ax.set_xticks(np.arange(0, 2 * np.pi + 0.01, np.pi / 4))
        plt.ylim([-2, 2])
        plt.show()
