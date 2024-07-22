class RowVectorFloat:
    def __init__(self,vector=[]):
        self.vector=vector
        for i in range(len(self.vector)):
             if isinstance(self.vector[i],str)==True:
                 try:
                     raise Exception('Entries can not be a string object')
                 except Exception as inst:
                     print(type(inst))
                     print(inst)
                     exit()



    def __str__(self):

        string=" ".join([str(x) for x in self.vector])
        return "{}".format(string)
    #To get iterbale object
    def __iter__(self):
        return iter(self.vector)
    # in order to get item
    def __getitem__(self, item):
        return self.vector[item]
    # in order to get the length
    def __len__(self):
        return(len(self.vector))
    # overloading the add function
    def __add__(self, other):
        for i in range(len(self.vector)):
            self.vector[i]=self.vector[i]+other.vector[i]
        return self

    # Overloading the multiplication function
    def __rmul__(self,other):
        vector=self.vector
        for i in range(len(vector)):
            self.vector[i]=other*self.vector[i]
        return self
    # Seeting value for a corresponding a key
    def __setitem__(self, key, value):
        self.vector[key]=value
        return self
    # in order to round of the digits to 2 significant digits
    def __round__(self, n=None):
        for i in range(len(self.vector)):
            self.vector[i]=round(self.vector[i],n)
        return self


r=RowVectorFloat([2,"3",4])
#print(r[2])
#r1=RowVectorFloat([1,4,5])
#r2=r1-2*r
#print(r2)
#print(r)
#r1=RowVectorFloat([2,3,4])
#r2=3*r1+2*r
#r=RowVectorFloat([])
#r[1]=7
#print(r)
#for i in range(4):
    #print("=i",i)
 #   for j in range(4):
  #      print("j=",j)
   #     list(r).append(0)
   # print(r)
    #list(r).clear()