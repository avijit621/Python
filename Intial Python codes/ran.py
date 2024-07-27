
import random
import matplotlib.pyplot as plt 
from matplotlib.pyplot import figure
import numpy as np
''''
dict ={}
keys = range(1,5)
labels=[x+1 for x in range(4)]
for i in keys:
   dict[i]=0
for i in range(100):
    r=random.randint(1,4)
    dict[r]=dict[r]+1
#print(dict)      
dist=[]
for i in range(4):
    #print(i)
    dist.append(dict[i+1]/100)
#print(dist)  
print(labels)
fig,ax=plt.subplots()
x=np.arange(len(labels))
width=0.35
#print(x)
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.bar(x,[100*i for i in dist])
plt.show()
'''
'''
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

labels = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [20, 34, 30, 35, 27]
women_means = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

fig, ax = plt.subplots()
ax.bar(x - width/2, men_means, width, label='Men')
ax.bar(x + width/2, women_means, width, label='Women')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()
plt.show()
'''
''''
class Arb:
    def __init__(self,num_sides=6):
        self.num_sides=num_sides
    def output(self):
        print(self.num_sides)

r = [random.random() for i in range(4)]
s = sum(r)
r = [ i/s for i in r ]
print(r)
print(sum(r))
'''
import random
a=[0.1,0.2,0.3,0.4]
px=[1,2,3,4]
b=[0.0,0.1,0.3,0.6,1]
d={}
for i in px:
    d[i]=0
#print(d)
for i in range(100):
   r=random.random()
#print(r)
   for i in range(len(b)):
      if (b[i]<r<b[i+1]):
        #print(i)
        d[i+1]=d[i+1]+1
new=[d[i]/100 for i in d.keys()]
print(new)