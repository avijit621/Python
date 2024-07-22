import matplotlib.pyplot as plt
import numpy as np
import random
class UndirectedGraph:
    def __init__(self,no_of_vertices=None):
        self.no_of_vertices=no_of_vertices
        self.adj_list={} # Adjacency list for the graph
        self.k = 0 # for counting the no of edges


    def __str__(self):
        string=[]
        # counting the no of edges
        for i in self.adj_list.keys():
            for j in self.adj_list[i]:
                if j >= i + 1:
                 self.k = self.k + 1
        # Prinitng for the free graph
        if self.no_of_vertices==None:
              self.no_of_vertices=len(self.adj_list.keys())
              string.append("graph with "+str(self.no_of_vertices)+" nodes and "+str(self.k)+
                            " edges.Neighbours of nodes are below")

              for i in self.adj_list.keys():
               temp="{" + ", ".join([str(x) for x in self.adj_list[i]]) + "}"
               string.append("Node "+str(i)+" :"+str(temp))
        # priniting for a graph with given vertices
        else:
            string.append("graph with " + str(self.no_of_vertices) + " nodes and " + str(self.k) +
                          " edges.Neighbours of nodes are below")
            for i in self.adj_list.keys():
                temp = "{" + ", ".join([str(x) for x in self.adj_list[i]]) + "}"
                string.append("Node " + str(i) + " :" + str(temp))
        return "\n".join(string)

    # Add node function
    def addNode(self,node_no):
        self.node_no=node_no
        # if no of vertices is specified checking to see node_no is
        # less than the number of nodes
        if self.no_of_vertices != None:
            if node_no <= self.no_of_vertices:
                self.adj_list[node_no] = []
            else:
               try:
                raise Exception('Node index cannot exceed number of nodes')
               except Exception as inst:
                   print(type(inst))
                   print(inst)
        # For a free graph assigning a empty list to the node
        else:
            self.adj_list[node_no]=[]
        return self

    # Add edge function
    def addEdge(self,*nodes):
       self.node=[*nodes]
       # When no of vertices are specified
       if self.no_of_vertices != None:
         for i in range(1, self.no_of_vertices+1):
             if i not in self.adj_list.keys(): # adding an node for the edge if its was added before
               self.adj_list[i] = []
         for i in range(1, self.no_of_vertices + 1):
             # updating the list for the nodes when it has not been added before
              if i == self.node[0] and self.node[1] not in self.adj_list[i]:
                self.adj_list[i].append(self.node[1])
              if i == self.node[1] and self.node[0] not in self.adj_list[i]:
                self.adj_list[i].append(self.node[0])
       # Free graphs we only add the node no for the edges specified
       else:
           if self.node[0] not in self.adj_list.keys():  # Checking whether a node if it was not already added
               self.adj_list[self.node[0]]=[]
           if self.node[1] not in self.adj_list.keys():
              self.adj_list[self.node[1]]=[]

           if self.node[1] not in self.adj_list[self.node[0]]:
             self.adj_list[self.node[0]].append(self.node[1])
           if  self.node[0] not in self.adj_list[self.node[1]]:
            self.adj_list[self.node[1]].append(self.node[0])

       return self

    # Operator Overloading
    def __add__(self, other):
        # checking whether a single argument was provided
        if  type(other)==int:

          self.adj_list[other]=[]
        else:
            # if not we store it in a list and use it later
            self.node=list(other)
            # Same logic as used in addEdge method
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

    # node distribution plotting via plotDegDist
    def plotDegDist(self):
        k=0
        degree_dist={} # storing the degree distribution
        self.node_degrees=[len(self.adj_list[i]) for i in self.adj_list.keys()]
        # populating degree distribution  which stores the degrees as keys
        # and the number  of vertices with that degree as its value

        for i in self.node_degrees:
            for j in self.adj_list.keys():
              if i == len(self.adj_list[j]):
                  k=k+1
            degree_dist[i]=k
            k=0

        degree_list = [i * degree_dist[i] for i in degree_dist.keys()]
        # finding aout average degree of the graph
        avg_degree = sum(degree_list) / len(self.adj_list.keys())
        # node degrees
        x = [i for i in range(len(self.adj_list.keys()))]
        # proportion of vertices
        y=[0 for  i in x]

        for i in range(len(x)):
          if x[i] in degree_dist.keys():
            y[i]=degree_dist[i]/len(self.adj_list.keys())
          else:
              y[i]=0
        # plotting of the graph
        fig,ax=plt.subplots()
        plt.scatter(x,y,s=5,color="b",label="Average degree distribution")
        plt.grid(True, which='both')
        plt.axvline(x=avg_degree,color="red",label="Avg. node")
        ax.legend()
        ax.set_xlabel("Node degree")
        ax.set_ylabel("Fraction of nodes")
        ax.set_title("Node degree distribution")
        plt.yticks(np.arange(0,max(y)+max(y)/5,max(y)/5))
        plt.xticks(np.arange(0,max(x)+self.no_of_vertices/5,self.no_of_vertices/5))

        plt.show()


class EERRandomGraph(UndirectedGraph):
    def __init__(self,no_of_vertices):
        self.vertices=no_of_vertices
        self.adj_list={}
        self.prob_par=0
        UndirectedGraph.__init__(self,self.vertices)
    def sample(self,prob_par):

        self.prob_par=prob_par
        for i in range(1,self.vertices+1):
            self.adj_list[i]=[]
        for i in range(1,self.vertices):
            for j in range(i+1,self.vertices+1):
                r =random.random()
                if r <prob_par:
                    self.adj_list[i].append(j)
                    self.adj_list[j].append(i)

        return self


g=EERRandomGraph(1000)
#g=g+(1,2)
#print(g)
g.sample(0.4)
#print(g)
g.plotDegDist()

