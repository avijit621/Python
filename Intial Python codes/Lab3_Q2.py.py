import random


class RowVectorFloat:
    def __init__(self, vector=[]):
        self.vector = vector

    def __str__(self):

        string = " ".join([str(x) for x in self.vector])
        return "{}".format(string)

    # To get iterbale object
    def __iter__(self):
        return iter(self.vector)

    # in order to get item
    def __getitem__(self, item):
        return self.vector[item]

    # in order to get the length
    def __len__(self):
        return (len(self.vector))

    # overloading the add function
    def __add__(self, other):
        for i in range(len(self.vector)):
            self.vector[i] = self.vector[i] + other.vector[i]
        return self

    # Overloading the multiplication function
    def __rmul__(self, other):
        vector = self.vector
        for i in range(len(vector)):
            self.vector[i] = other * self.vector[i]
        return self

    # Seeting value for a corresponding a key
    def __setitem__(self, key, value):
        self.vector[key] = value
        return self

    # in order to round of the digits to 2 significant digits
    def __round__(self, n=None):
        for i in range(len(self.vector)):
            self.vector[i] = round(self.vector[i], n)
        return self


class SquareMatrixFloat:
    def __init__(self, rows):
        self.rows = rows
        self.matrix = {i: [] for i in range(rows)}
        s = [0 for i in range(rows)]
        r = RowVectorFloat(s)
        for i in range(rows):
            self.matrix[i] = r
        if  isinstance(self.rows,str)==True or self.rows<=0:
            try:
                raise Exception('No of rows need to be integer "')
            except Exception as inst:
                print(type(inst))
                print(inst)
                exit()

    def __str__(self):
        strings = []
        strings.append("The matrix is ")
        for i in range(self.rows):
            strings.append(str(round(self.matrix[i], 2)))
        return "\n".join(strings)

    # Sampling a symmetric matrix
    def sampleSymmetric(self):
        # Setting the non diagonal values uniformly from (0,n)
        for i in self.matrix.keys():
            s = list(self.matrix[i])
            r = random.random()
            while r == 0:
                r = random.random()
            s[i] = round(4 * r, 2)
            self.matrix[i] = RowVectorFloat(s)
        # making sure the matrix is symmetric and the
        # diagonal entries are uniformly sampled from (0,1)
        for i in self.matrix.keys():
            for j in range(self.rows):
                if [i, j] != [j, i]:
                    r = round(random.random(), 2)
                    while r == 0:
                        r = random.random()
                    self.matrix[i][j] = r
                    self.matrix[j][i] = r

        return self

    # Reducing the matrix two row reduced echelon from
    def toRowEchelonForm(self):
        for i in self.matrix.keys():
            # Making the diagonal entries 1 at each i th iteration
            self.matrix[i] = (1 / self.matrix[i][i]) * self.matrix[i]
            for j in range(self.rows):

                if j > i:
                    pivot = self.matrix[j][i]
                    self.matrix[j] = self.matrix[j] + (-pivot) * self.matrix[i]
                    self.matrix[i] = (-1 / pivot) * self.matrix[i]  # making sure the i th entry of the
                    # matrix stays same
        for i in self.matrix.keys():
            for j in range(self.rows):
                if self.matrix[i][j] == -0.0:
                    self.matrix[i][j] = abs(self.matrix[i][j])

        return self

    # hecking teh matrix is row dominant or not
    def isDRDominant(self):
        k = 0
        for i in self.matrix.keys():
            s = list(self.matrix[i])
            if s[i] < sum(s) - s[i]:
                return False
            else:
                k = k + 1
            s.clear()

        if k == self.rows:
            return True

    # Using jacobi method to solve it
    def jSolve(self, b, iter):
        self.b = b
        self.iter = iter
        # checking the matrix is diagonally dominant or not
        for i in self.matrix.keys():
            s = list(self.matrix[i])
            if s[i] < sum(s) - s[i]:
                try:
                    raise Exception('Not solving because convergence not guranteed')
                except Exception as inst:
                    print(type(inst))
                    print(inst)
                    exit()

        D = [0 for i in range(self.rows)]
        # Getting the diagonal entries of the matrix
        for i in self.matrix.keys():
            D[i] = self.matrix[i][i]
        zero_list = [0 for i in range(self.rows)]
        # intiializing the lower and upper triangular matrix
        l = {i: list(self.matrix[i]) for i in self.matrix.keys()}
        u = {j: list(self.matrix[j]) for j in self.matrix.keys()}
        t = {i: zero_list for i in range(self.rows)}
        # Populating the lower and upper triangular matrix
        for i in self.matrix.keys():
            for j in range(self.rows):
                if i >= j:
                    u[i][j] = 0
        for i in self.matrix.keys():
            for j in range(self.rows):
                if i <= j:
                    l[i][j] = 0
        # Forming the matrix T=-D^(-1)(L+U)

        for i in range(self.rows):
            t[i] = (-1 / D[i]) * (RowVectorFloat(l[i]) + RowVectorFloat(u[i]))

       # making the matrix D^(-1)b
        c = []
        for i in range(self.rows):
            c.append((1 / D[i]) * self.b[i])
        C = RowVectorFloat(c)
        s = 0
        add = 0
        b = []
        error = []
        total_err = []
        # intializing the initial vector as 1's
        x_sol = RowVectorFloat([1 for i in range(self.rows)])

        k = 0
        # iterating s given by the user
        while (k != self.iter):
            for i in range(self.rows):
                for j in range(self.rows):
                    # multiplying T and X_sol
                    s = s + t[i][j] * x_sol[j]
                b.append(s)
                s = 0
            # iterating solutions
            x_sol = C + RowVectorFloat(b)
            # calulating || Ax^(k)-b|| for each iteration
            for i in range(self.rows):
                for j in range(self.rows):
                    add = add + self.matrix[i][j] * x_sol[j]
                error.append((add - self.b[i]) ** 2)
                add = 0
            # getting toatl error
            total_err.append(sum(error) ** (1 / 2))

            k = k + 1

        return total_err, list(x_sol)


s = SquareMatrixFloat(-4)
#s.sampleSymmetric()
# s1.toRowEchelonForm()
# print(s.isDRDominant())
# s1.toRowEchelonForm()
#print(s)
#(e, x) = s.jSolve([1, 2, 3, 4], 15)
#print(e)
#print(x)
# print(s)
