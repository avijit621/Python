import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline, BSpline
class Polynomial:
    def __init__(self,list_co=[]):
        self.list_co=list_co

    def __str__(self):
        strings=[]
        strings.append("Coefficients of the polynomial are:")
        temp =  " ".join([str(x) for x in self.list_co])
        strings.append(str(temp))
        return "\n".join(strings)
    # setting getitem properly to return evaluated value for a polynomial
    def __getitem__(self, item):
        return sum([(item ** i) * self.list_co[i] for i in range(len(self.list_co))])
    def __add__(self, other):
        for i in range(len(self.list_co)):
            self.list_co[i]=self.list_co[i]+other.list_co[i]
        return self
    def __sub__(self, other):
        for i in range(len(self.list_co)):
            self.list_co[i]=self.list_co[i]-other.list_co[i]
        return self

    def __rmul__(self, other):
        vector = self.list_co
        for i in range(len(vector)):
            self.list_co[i] = other * self.list_co[i]
        return self
    def __mul__(self, other):
        r1=len(self.list_co)
        r2=len(other.list_co)
        prod=[0]*(r1+r2-1)
        for i in range(r1):
            for j in range(r2):
                prod[i+j]+=self.list_co[i]*other.list_co[j]
        self.list_co=prod
        return self
    def show(self,a,b):
        self.a=a
        self.b=b
        r=(self.b-self.a)/5
        x=np.arange(self.a,self.b+r,r)
        p=Polynomial(self.list_co)
        y=[p[i]for i in x]
        fig,ax=plt.subplots()
        ax.plot(x,y)
        s=[p[self.a],p[self.b]]
        s.sort()
        ax.set_ylim(s)
        ax.set_xlabel("x")
        ax.set_ylabel("p(x)")

        ax.set_title("Plot of the Polynomial")
        ax.set_xlim(self.a,self.b)
        plt.grid(True,which="both")
        plt.show()

    def fitViaMatrixMethod(self,plot_val):
        self.plot_val=plot_val
        x_val=[]
        y_val=[]
        s=[]
        for i in range (len(self.plot_val)):
            x_val.append(self.plot_val[i][0])
            y_val.append(self.plot_val[i][1])
        for i in range(len(self.plot_val)):
             s.append([x_val[i]**j for j in range(len(self.plot_val))])
        A=np.array(s)
        b=np.array(y_val)
        x=np.linalg.solve(A,b)
        p=Polynomial(x)
        fig,ax=plt.subplots()
        r=(max(x_val)-min(x_val))/5
        x=np.arange(min(x_val),max(x_val)+0.5,0.5)
        ax.plot(x_val,y_val,"ro")
        y=[p[i] for  i in x]
        ax.set_ylabel("p(x)")
        ax.set_xlabel("x")
        ax.set_title("Polynomial interpolation using matrix method")
        plt.grid(True, which="both")
        xnew = np.linspace(x.min(), x.max(), 300)

        spl = make_interp_spline(x, y, k=3)  # type: BSpline
        y_smooth = spl(xnew)

        plt.plot(xnew, y_smooth)
        plt.show()

    def fitViaLagrangePoly(self,plo_val):
        self.plot_val=plo_val
        x_val = []
        y_val = []
        s = []
        a=Polynomial([])
        for i in range(len(self.plot_val)):
            x_val.append(self.plot_val[i][0])
            y_val.append(self.plot_val[i][1])
        for i in  range(len(self.plot_val)):
            for j in range(len(x_val)):
                if j!=i:
                    #print(Polynomial([x_val[j],1]))
                    a*=Polynomial([x_val[j],1])
            s.append(a)

        print (list(s[0]))










#p1=Polynomial([-1,1])
#p2=Polynomial([1,1,1])
#p=p1*p2
#print(p)
#p=Polynomial([1,0,1])
#p.show(1,2)
p=Polynomial([])
#p.fitViaMatrixMethod([(0,1), (1,4), (-1, 0), (2, 15),(3,12)])
p.fitViaLagrangePoly([(0,1), (1,4), (-1, 0), (2, 15),(3,12)])