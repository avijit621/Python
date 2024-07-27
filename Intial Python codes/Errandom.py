import matplotlib.pyplot as plt
import numpy as np
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
        #self.
        if self.no_of_vertices==None:
              self.no_of_vertices=len(self.adj_list.keys())
              string.append("graph with "+str(self.no_of_vertices)+" nodes and "+str(self.k)+
                            " edges.Neighbours of nodes are below")
              #string.append()
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
       #print(self.adj_list)
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
        #self.node=other
        if  type(other)==int:
          #if self.no_of_vertices==None:
             #self.no_of_vertices=0
          #self.no_of_vertices = self.no_of_vertices + other
          self.adj_list[other]=[]
        else:
            #print("1")
            self.node=list(other)
           # print(self.node)
            if self.no_of_vertices==None:
               # print("2")
                if self.node[0] not in self.adj_list.keys():
                    self.adj_list[self.node[0]] = []
                if self.node[1] not in self.adj_list.keys():
                    self.adj_list[self.node[1]] = []
                if self.node[1] not in self.adj_list[self.node[0]]:
                  self.adj_list[self.node[0]].append(self.node[1])
                if self.node[0] not in self.adj_list[self.node[1]]:
                   self.adj_list[self.node[1]].append(self.node[0])
            else:
                #print("3")
                for i in range(1, self.no_of_vertices+1):
                    if i not in self.adj_list.keys():
                      self.adj_list[i] = []
                for i in range(1, self.no_of_vertices + 1):
                    if i == self.node[0] and self.node[1] not in self.adj_list[i]:
                        #print("4")
                        self.adj_list[i].append(self.node[1])
                        #print(self.adj_list[i])
                    if i == self.node[1] and self.node[0] not in self.adj_list[i]:
                        self.adj_list[i].append(self.node[0])

        return self

    def plotDegDist(self):
        k=0
        degree_dist={}
        self.node_degrees=[len(self.adj_list[i]) for i in self.adj_list.keys()]
        #print (self.node_degrees)
        for i in self.node_degrees:
            for j in self.adj_list.keys():
              if i == len(self.adj_list[j]):
                  k=k+1
            degree_dist[i]=k
            k=0
        #y=[degree_dist[i]/self.no_of_vertices for i in degree_dist.keys()]
        #x=[i for i in degree_dist.keys()]
        #print(list(degree_dist.keys()))
        degree_list = [i * degree_dist[i] for i in degree_dist.keys()]
        #print(degree_list)
        avg_degree = sum(degree_list) / len(self.adj_list.keys())
        #print(avg_degree)
        x = [i for i in range(round(avg_degree) + 4)]
        #print(x)
        #x=[i for i in range(self.no_of_vertices) ]
        y=[0 for  i in x]
        #print(y)
        for i in x:
          if i in degree_dist.keys():
            y[i]=degree_dist[i]/len(self.adj_list.keys())
          else:
              y[i]=0
        #print(y)



        #print(x)
        fig,ax=plt.subplots()
        ax.plot(x,y,"bo",label="Average degree distribution")
        plt.grid(True, which='both')
        plt.axvline(x=avg_degree,color="red",label="Avg. node")
        ax.legend()
        ax.set_xlabel("Node degree")
        ax.set_ylabel("Fraction of nodes")
        ax.set_title("Node degree distribution")
        plt.yticks(np.arange(0,max(y)+0.1,0.1))
        plt.xticks(np.arange(0,max(x)+0.5,0.5))

        plt.show()
        #print(x)
        #print(y)

class EERRandomGraph(UndirectedGraph):
    def __init__(self,prob_value):
        UndirectedGraph.__init__(self,no_of_vertices=None)
     def smple(self,prob_par):
         self.pob_par=prob_par



g=EERRandomGraph(100)
#g=g+(1,2)
print(g)

