import matplotlib.pyplot as plt
import numpy as np
import random
class UndirectedGraph:
    def __init__(self,no_of_vertices=None):
        self.no_of_vertices=no_of_vertices
        self.adj_list={}
        self.k = 0



    def __str__(self):
        string=[]
        for i in self.adj_list.keys():
            for j in self.adj_list[i]:
                if j >= i + 1:
                 self.k = self.k + 1

        if self.no_of_vertices==None:
              self.no_of_vertices=len(self.adj_list.keys())
              string.append("graph with "+str(self.no_of_vertices)+" nodes and "+str(self.k)+
                            " edges.Neighbours of nodes are below")

              for i in self.adj_list.keys():
               temp="{" + ", ".join([str(x) for x in self.adj_list[i]]) + "}"
               string.append("Node "+str(i)+" :"+str(temp))
        else:
            string.append("graph with " + str(self.no_of_vertices) + " nodes and " + str(self.k) +
                          " edges.Neighbours of nodes are below")
            for i in self.adj_list.keys():
                temp = "{" + ", ".join([str(x) for x in self.adj_list[i]]) + "}"
                string.append("Node " + str(i) + " :" + str(temp))
        return "\n".join(string)

    def addNode(self,node_no):
        self.node_no=node_no
        if self.no_of_vertices != None:
            if node_no <= self.no_of_vertices:
                self.adj_list[node_no] = []
            else:
               try:
                raise Exception('Node index cannot exceed number of nodes')
               except Exception as inst:
                   print(type(inst))
                   print(inst)
        else:
            self.adj_list[node_no]=[]
        return self
    def addEdge(self,*nodes):
       self.node=[*nodes]

       if self.no_of_vertices != None:
         for i in range(1, self.no_of_vertices+1):
             if i not in self.adj_list.keys():
               self.adj_list[i] = []
         for i in range(1, self.no_of_vertices + 1):
              if i == self.node[0] and self.node[1] not in self.adj_list[i]:
                self.adj_list[i].append(self.node[1])
              if i == self.node[1] and self.node[0] not in self.adj_list[i]:
                self.adj_list[i].append(self.node[0])

       else:
           if self.node[0] not in self.adj_list.keys():
               self.adj_list[self.node[0]]=[]
           if self.node[1] not in self.adj_list.keys():
              self.adj_list[self.node[1]]=[]

           if self.node[1] not in self.adj_list[self.node[0]]:
             self.adj_list[self.node[0]].append(self.node[1])
           if  self.node[0] not in self.adj_list[self.node[1]]:
            self.adj_list[self.node[1]].append(self.node[0])

       return self

    def __add__(self, other):

        if  type(other)==int:

          self.adj_list[other]=[]
        else:

            self.node=list(other)

            if self.no_of_vertices==None:

                if self.node[0] not in self.adj_list.keys():
                    self.adj_list[self.node[0]] = []
                if self.node[1] not in self.adj_list.keys():
                    self.adj_list[self.node[1]] = []
                if self.node[1] not in self.adj_list[self.node[0]]:
                  self.adj_list[self.node[0]].append(self.node[1])
                if self.node[0] not in self.adj_list[self.node[1]]:
                   self.adj_list[self.node[1]].append(self.node[0])
            else:

                for i in range(1, self.no_of_vertices+1):
                    if i not in self.adj_list.keys():
                      self.adj_list[i] = []
                for i in range(1, self.no_of_vertices + 1):
                    if i == self.node[0] and self.node[1] not in self.adj_list[i]:

                        self.adj_list[i].append(self.node[1])

                    if i == self.node[1] and self.node[0] not in self.adj_list[i]:
                        self.adj_list[i].append(self.node[0])

        return self

    def plotDegDist(self):
        k=0
        degree_dist={}
        self.node_degrees=[len(self.adj_list[i]) for i in self.adj_list.keys()]

        for i in self.node_degrees:
            for j in self.adj_list.keys():
              if i == len(self.adj_list[j]):
                  k=k+1
            degree_dist[i]=k
            k=0

        print(degree_dist)
        degree_list = [i * degree_dist[i] for i in degree_dist.keys()]

        avg_degree = sum(degree_list) / len(self.adj_list.keys())

        x = [i for i in range(len(self.adj_list.keys()))]

        y=[0 for  i in x]

        for i in range(len(x)):
          if x[i] in degree_dist.keys():
            y[i]=degree_dist[i]/len(self.adj_list.keys())
          else:
              y[i]=0





        fig,ax=plt.subplots()
        ax.plot(x,y,"bo",label="Average degree distribution")
        plt.grid(True, which='both')
        plt.axvline(x=avg_degree,color="red",label="Avg. node")
        ax.legend(loc="upper right")
        ax.set_xlabel("Node degree")
        ax.set_ylabel("Fraction of nodes")
        ax.set_title("Node degree distribution")
        plt.yticks(np.arange(0,max(y)+0.1,0.1))
        plt.xticks(np.arange(0,max(x)+((max(x)-min(x))/(2*max(x))),((max(x)-min(x))/(2*max(x)))))
        plt.show()




    def BFSUtil(self, temp, v, visited):
        # Mark the current vertex as visited
        visited[v-1] = True

        # Store the vertex to list
        temp.append(v)

        # Repeat for all vertices adjacent
        # to this vertex v
        for i in self.adj_list[v]:
            if visited[i-1] == False:
                # Update the list
                temp = self.BFSUtil(temp, i, visited)
        return temp

    def oneTwoCompomentSizes(self):
        visited = []
        cc = []
        for i in range(self.no_of_vertices):
            visited.append(False)
        for v in range(self.no_of_vertices):
            if visited[v] == False:
                temp = []
                cc.append(self.BFSUtil(temp, v+1, visited))
        len_cc=[len(i) for i in cc ]
        len_cc.sort(reverse=True)

        return [len_cc[0],len_cc[1]]

class EERRandomGraph(UndirectedGraph):
    def __init__(self,no_of_vertices):
        self.vertices=no_of_vertices
        self.adj_list={}
        self.prob_par=0
        UndirectedGraph.__init__(self,self.vertices)
    def sample(self,prob_par):
        #self.adj_list={}
        #print(self.no_of_vertices)
        self.prob_par=prob_par
        for i in range(1,self.vertices+1):
            self.adj_list[i]=[]
        for i in range(1,self.vertices):
            for j in range(i+1,self.vertices+1):
                r =random.random()
                if r <prob_par:
                    self.adj_list[i].append(j)
                    self.adj_list[j].append(i)
                #print("i=",i,"j=",j)
        #print(self.adj_list)
        return self

#g=UndirectedGraph(6)
#g=g+(1,2)
#g=g+(3,4)
#g=g+(3,4)
#g=g+(6,4)
g=EERRandomGraph(100)
g.sample(0.01)
print(g.oneTwoCompomentSizes())


