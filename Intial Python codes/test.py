# Python program to combine two dictionary
# adding values for common keys
# initializing two dictionaries
import numpy as np

''''
dict1 = {'a': 12, 'for': 25, 'c': 9, "Geeks": 300}
dict2 = {'Geeks': 100, 'geek': 200, 'for': 300, "a": 15}

#a=10
#print(len(list(a)))
a={1: [2, 3], 2: [1, 3, 4, 7], 3: [2, 1], 4: [5, 2], 5: [4], 7: [2]}
k=0
for i in a.keys():
            for j in a[i]:
              if j >= i + 1:
                 k = k + 1

print(k)
for i in a.keys():
    temp= "{" + ", ".join([str(x) for x in a[i]]) + "}"
    print(temp)
'''

# r=dict1['a'].append(13)
# print(None+10)
'''
#adding the values with common key
for key in dict2:
    if key in dict1:
        dict2[key] = dict2[key] + dict1[key]
    else:
        pass
dict1.update(dict2)
print(dict1)

#dict1.pop("a")
#print(dict1)
'''
'''
l1=[1,2,3,3,2,2,4,4,5,3,9]
l2=[10,20,30,30,20,20,40,40,50,30,90]
s=[]
l=[]
x=0
res={}
[s.append(x) for x in l1 if x not in s]
print(s)
for i in range(0,len(s)):
    for j in range(0,len(l1)):
        if s[i] == l1[j]:
          #print (j)
          l.append(j)
        else:
             pass
    #print("end of ",i, " iteration")
    if len(l)>1:
     #print(l)
     for k in range(0,len(l)):
          x=x+l2[l[k]]
     #break
    res[s[i]]=x
    x = 0
    l.clear()
    #print(l)


#print(list(res.keys()))
for i in range(0, len(l1)):
    #print (i)
    if res[l1[i]]==0:
        #print(l1(i))
        d={l1[i]: l2[i]}
        #print (d)
        #print (i)
        res.update(d)

print(res)
'''
'''import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(1)
x = np.linspace(0, 2*np.pi, 1001)
z=np.sin(x)
plt.plot(x, z)
plt.xlim(0,  2*np.pi)
plt.grid(True, which='both')
plt.axhline(y=1, color='g',label="Maximum value")
plt.axhline(y=0, color='k')
plt.axhline(y=-1, color='r',label="minimum value")

plt.xticks([0,np.pi/4,np.pi/2,3*np.pi/4,np.pi,5*np.pi/4,3*np.pi/2,7*np.pi/4,2*np.pi],
             [r'$0$', r'$\pi/4$', r'$\pi/2$', r'$3\pi/4$', r'$\pi$',r'$5\pi/4$',
                r'$3\pi/2$',r'$7\pi/4$',r'$2\pi$'])
ax.legend()
plt.ylim([-2, 2])
#plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi],
          # [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])
plt.show()


'''
'''
from scipy.stats import binom
# setting the values
# of n and p
n = 100
p = 0.7
# defining the list of r values
r_values = list(range(n + 1))
# obtaining the mean and variance
mean, var = binom.stats(n, p)
# list of pmf values
dist = [binom.pmf(r, n, p)*n for r in r_values ]
# printing the table
print("r\tn*p(r)")
for i in range(0,n + 1,20):
    print(str(r_values[i]) + "\t" + str(dist[i]))
# printing mean and variance
print("mean = "+str(mean))
print("variance = "+str(var))
print(max(dist))
'''


# Python program to print connected
# components in an undirected graph


# Python program to print connected
# components in an undirected graph


class Graph:

    # init function to declare class variables
    def __init__(self, V):
        self.V = V
        self.adj = [[] for i in range(1,V+1)]
    def __str__(self):
        return  "{}".format(self.adj)


    def DFSUtil(self, temp, v, visited):

        # Mark the current vertex as visited
        visited[v-1] = True

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj[v-1]:
            #print("inside BFS",i)
            if visited[i-1] == False:
                # Update the list
                temp = self.DFSUtil(temp, i, visited)
        return temp

    # method to add an undirected edge
    def addEdge(self, v, w):
        self.adj[v-1].append(w)
        self.adj[w-1].append(v)

    def connectedComponents(self):
        visited = []
        cc = []
        for i in range(self.V):
            visited.append(False)
        print(visited)
        for v in range(self.V):
            if visited[v] == False:
                temp = []
                print(v)
                cc.append(self.DFSUtil(temp, v+1, visited))
        #print(cc)
        return cc


# Driver Code
if __name__ == "__main__":
    # Create a graph given in the above diagram
    # 5 vertices numbered from 0 to 4
    g = Graph(5)
    g.addEdge(2, 1)
    g.addEdge(3, 4)
    g.addEdge(4, 5)
    print(g)
    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)


# This code is contributed by Abhishek Valsan
