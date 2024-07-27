from RowVectorFloat import *
import random
class RowVectorFloat:
    def __init__(self,vector=[]):
        self.vector=vector



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

class SquareMatrixFloat:
    def __init__(self, rows):
        self.rows = rows
        self.matrix = {i: [] for i in range(rows)}
        s = [0 for i in range(rows)]
        r = RowVectorFloat(s)
        for i in range(rows):
            self.matrix[i] = r

    def __str__(self):
        strings = []
        strings.append("The matrix is ")
        for i in range(self.rows):
            strings.append(str(round(self.matrix[i], 2)))
        return "\n".join(strings)
    # sample a matrix with uniform values as mentioned in question
    def sampleSymmetric(self):

        # Setting the non-diagonal digits uniformly from (0,n)
        for i in self.matrix.keys():
            s = list(self.matrix[i])
            r = random.random()
            while r == 0:
                r = random.random()
            s[i] = round(4 * r, 2)
            self.matrix[i] = RowVectorFloat(s)
        # Setting the diagonal elements uniformly from (0,1)
        for i in self.matrix.keys():
            for j in range(self.rows):
                if [i, j] != [j, i]:
                    r = round(random.random(), 2)
                    while r == 0:
                        r = random.random()
                    self.matrix[i][j] = r
                    self.matrix[j][i] = r

        return self
    # Reducing the matrix to row reduced echelon form
    def toRowEchelonForm(self):
        for i in self.matrix.keys():
            # at each iteration setting the diagonal entry to 1
            self.matrix[i] = (1 / self.matrix[i][i]) * self.matrix[i]
            # using the properties RowVectorfloat to set values to zero
            for j in range(self.rows):

                if j > i:
                    pivot = self.matrix[j][i]
                    self.matrix[j] = self.matrix[j] + (-pivot) * self.matrix[i]
                    self.matrix[i] = (-1 / pivot) * self.matrix[i]
        # Setting the negative zeroes to +ve zeroes
        for i in self.matrix.keys():
            for j in range(self.rows):
                if self.matrix[i][j] == -0.0:
                    self.matrix[i][j] = abs(self.matrix[i][j])

        return self
     # checking whether the matrix is Row dominant
    def isDRDominant(self):
        k = 0
        for i in self.matrix.keys():
            s = list(self.matrix[i])
            # checking if the diagonal element is less than the
            # sum of other entries in the row
            if s[i] < sum(s) - s[i]:
                return False
            else:
                k = k + 1
            s.clear()

        if k == self.rows:
            return True
    # Jacobi solve method
    def jSolve(self,b,iter):
         self.b=b
         self.iter=iter
         # getting the diagonal entries
         D=[0 for i in range(self.rows)]
         for i in self.matrix.keys():
             D[i]=self.matrix[i][i]
         zero_list=[0 for i in range(self.rows)]
         # intializing the Lower triangular matrix
         l={i:list(self.matrix[i]) for i in self.matrix.keys()}
         # Intializing the upper triangular matrix
         u={j:list(self.matrix[j]) for j in self.matrix.keys()}
         # Intializing the matrix T=-D^(-1)(L+U)
         t={i:zero_list for i in range(self.rows)}
         # Populating entries for upper and lower traingular matrix
         for i in self.matrix.keys():
            for j in range(self.rows):
                if i>=j:

                  u[i][j]=0
         for i in self.matrix.keys():
            for j in range(self.rows):
                    if i <= j:
                        # print(i,j)
                        l[i][j] = 0
         for i in range(self.rows):
             t[i]=(-1/D[i])*(RowVectorFloat(l[i])+RowVectorFloat(u[i]))

        










s = SquareMatrixFloat(3)
s.sampleSymmetric()
# s1.toRowEchelonForm()
#print(s.isDRDominant())
# s1.toRowEchelonForm()
print(s)
s.jSolve([1,2,3,4],10)
#print(s)