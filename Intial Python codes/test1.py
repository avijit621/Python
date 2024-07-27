'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

class Sine:
    def __init__(self):
        self.sine_list = [] # list storing arguments of the sine function
        self.sine_label = [] # This list is used as label in the plot


    def addSine(self, angle): # addSine creates a list corresponding the angles
        self.angle = angle    # which  have been added to the sine object
        self.sine_list.append(self.angle)
        return self

    def shiftRight(self, shift_angle): # This method shifts the sine values to right
        self.shift_angle=shift_angle
        for i in range(len(self.sine_list)):
            self.sine_list[i]=self.sine_list[i]-self.shift_angle # for shifting right we subtract the shift_angle
        return self                                              # from the values already stored
                                                                 # owing to transformation x =y+h
    def shiftLeft(self, shift_angle):
        self.shift_angle=shift_angle
        for i in range(len(self.sine_list)):
            self.sine_list[i]=self.sine_list[i]+self.shift_angle # for shifting left we add the shift_angle
        return self                                              # to the values already stored
                                                                 # owing to transformation x =y-h

    def show(self):
        self.sine_label = self.sine_list
        z = []
        for angle in self.sine_list:
            x = np.linspace(0, 2*np.pi, 1001)
            z.append(np.sin(x + np.pi/180 * angle)) # the list z stores all the values to be plotted
        # The range is set to 0 to 2pi
        x = np.linspace(0, 2*np.pi, 1001)
        fig, ax = plt.subplots(1)
        for i in range(len(z)): # we plot all the sines that has been provided by uing for loop

            plt.plot(x, z[i], label=r"$\phi$="+str(self.sine_label[i]))
            plt.xlim(0, 2*np.pi)
            plt.xlabel(r"$\theta$")
            plt.ylabel(r"$\sin(\theta+\phi)$")
            plt.title("Interactive sinusodial functions")
            plt.grid(True, which='both')
            plt.axhline(y=1, color='g',)
            plt.axhline(y=0, color='k')
            plt.axhline(y=-1, color='r')
            # Setting the ticks for x axis as multiples of pi
            plt.xticks(
                [0, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi, 5 * np.pi / 4, 3 * np.pi / 2, 7 * np.pi / 4, 2 * np.pi],
                [r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$', r'$5\pi/4$',
                 r'$3\pi/2$', r'$7\pi/4$', r'$2\pi$'])
            ax.legend()
            plt.ylim([-2, 2])

        plt.show()



s = Sine()
s.addSine(0)
s.addSine(90)
#s.show()
#s.shiftRight(45)
#s.shiftLeft(45)
s.show()
#print(np.sin(135))
'''

'''
# Python program to print connected
# components in an undirected graph


class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(V)]
    def __str__(self):
        return "{}".format(self.adj)

    def addEdge(self, v, w):
        self.adj[v].append(w)
        self.adj[w].append(v)


g = Graph(5)
g.addEdge(1, 0)
g.addEdge(2, 3)
g.addEdge(3, 4)
# cc = g.connectedComponents()
print("Following are connected components")
# print(cc)
print(g)
'''
from RowVectorFloat import *
d={}
d[0]=RowVectorFloat([4,2,3])
d[1]=RowVectorFloat([4,11,6])
d[2]=RowVectorFloat([2,3,11])

#d={0:[1,2,3],1:[4,5,6],2:[2,3,11]}
#print(d)
'''
for i in d.keys():
    for j in range(3):
        # pass
        if j != i:
            print("j=",j)
            pivot = d[j][i] / d[i][i]
            print("Pivot=",pivot)
            print("before operation i=", i, "|", d[i])
            d[j] = d[j] + (-pivot) * d[i]
            d[i]=(-1/pivot)*d[i]
            print("self.matrix[", j, "]", d[j])
            print("after operation i=", i, "|", d[i])
for i in d.keys():
    (1/d[i][i]) *d[i]




print(d[0])
print(d[1])
print(d[2])
'''
k=0
for i in d.keys():
    s=list(d[i])
    if s[i]<sum(s)-s[i]:
        #print("False")
        break
    else:
        k=k+1
if k==3:
    print("True")

#print("True")

prod = [0] * (3 + 4 - 1)
#print(prod)
a=[1,2,3,4]
b=sum([(2**i)*a[i] for i in range(len(a))])
#print(b)
print(0**0)