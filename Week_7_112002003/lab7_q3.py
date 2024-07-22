# biection method to find nth root of a integer 
def Bisection(n,a,err):
    # checking whether n th root can be found or not
    if a<0 and (a%2==0 and n%2==0):
        try:
            raise Exception(str(n)+"th root does not exist ")
        except Exception as inst:
                print(type(inst))
                print(inst)
        return None
    if a >0:
       an=0
       bn=a
    else:
        an=a
        bn=0
    # nth root of a  means finding the solution of x^n-a
    f= lambda x: x**n -a
    # implementing bisection to approximate the solution of f
    while(abs(an-bn) >err):
        cn=(an+bn)/2
        if (f(cn)<0 and f(an)<0) or (f(cn)>0 and f(an)>0):
            an=cn
        else:
            bn=cn
    print("The",n,"th root of",a,"is",(an+bn)/2)
Bisection(4,1024,0.0001)