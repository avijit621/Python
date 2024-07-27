class Paper:
    def __init__(self, area):
        self.total_area = area
        self.rem_area = area
        self.area_list = []  # List to store the areas of the polygon provided
        self.num_sides = []  # List to store the num_sides of the polygon provided
        self.res = {} # A dictionary to store the values in a suitable manner
        self.key = 0 # key to print the values according as merge or erase is called

        if self.total_area < 0:
            try:
                raise Exception('Paper should have positive area') # exception handling to check whether paper has
            except Exception as inst:                               # positive area
                print(type(inst))
                print(inst)


    def __str__(self):
        strings=[] # an empty list to used to print the details
        if self.rem_area < 0: # Exception handling to check whether paper is overloaded with the given polygons
            try :
                raise Exception("The Paper does not have sufficient area to fit polygon")
            except Exception as inst:
                print(type(inst))
                print(inst)
                # printing the details after merge is called
        elif self.key == 1:
            strings.append("Paper now has free area "+str(self.rem_area)+" out of "+str(self.total_area)+" and contains:")
            for key, value in self.res.items():
                if key != 3:
                    strings.append("Polygon with sides "+str(key)+" and area "+str(value))
                else:
                    strings.append("Triangle with area "+str(value))
             # printing the details after erase is called
        elif self.key == 2:
            strings.append("Paper now has free area "+str(self.rem_area)+" and contains:")
        else:
            strings.append("Paper has free area "+str(self.rem_area)+" out of "+str(self.total_area)+
                           " and contains")
            for i in range(0,len(self.num_sides)):
                if self.num_sides[i] == 3:
                    strings.append("Triangle with area "+str(self.area_list[i]))
                else:
                    strings.append("Polygon with sides "+ str(self.num_sides[i])+" and area "
                                                                          +str(self.area_list[i]))
        return '\n'.join(strings) # finally returning after joining all the details

    def __add__(self, other): # operator Overloading
        self.num_sides.append(other.num_sides)
        self.area_list.append(other.area)
        self.rem_area = self.rem_area - other.area
        if self.rem_area < 0: # checking to see whether paper has enough free space
            try:
                raise Exception('Paper does not have enough free area to fit polygon')
            except Exception as inst:
                print(type(inst))
                print(inst)
        else:
            return self

    def merge(self):
        s = []
        l = []
        x = 0
        self.key=1
        [s.append(x) for x in self.num_sides if x not in s] # creating a unique list containing distinctt num_sides
                                                             # of all the polygons provided

        for i in range(0, len(s)): # using this list to check whether there are polygons of same sides
            for j in range(0, len(self.num_sides)):
                if s[i] == self.num_sides[j]:
                    l.append(j) # creating a list l which has indices  of the duplicates
                else:
                    pass
            if len(l) > 1: # if there are duplicates length of l is more than 1
                for k in range(0, len(l)):
                    x = x + self.area_list[l[k]] # using the indices stored in l we sum the areas
            self.res[s[i]] = x
            x = 0
            l.clear()
        for i in range(0, len(self.num_sides)):
            # print (i)
            if self.res[self.num_sides[i]] == 0:
                self.res.update({self.num_sides[i]: self.area_list[i]}) # creating a dictionary which has unique values
        return self.res, self.key
     # Erase function
    def erase(self):
        self.key = 2
        for key,value in self.res.items(): # using our already populated dictionary to erase the paper
            self.rem_area=self.rem_area+value
        return self.key,self.rem_area

# Polygon class retianed from previous Question
class Polygon:
    def __init__(self, num_sides, area):
        self.num_sides = num_sides
        self.area = area

        if self.area < 0:
            try:
                raise Exception("Polygon should have positive area")
            except Exception as inst:
                print(type(inst))
                print(inst)
        elif self.num_sides < 3:
            try:
                raise Exception("Number of sides should be at least 3")
            except Exception as inst:
                print(type(inst))
                print(inst)
        else:
            pass

    def __str__(self):
            return "Polygon with sides {0} and area {1}".format(self.num_sides, self.area)
 
# triangle class retained from prvious question
class Triangle(Polygon):
    def __init__(self, a, b, c):
        self.area_indicator= 0
        self.a = a
        self.b = b
        self.c = c
        if (self.a + self.b > self.c) and (self.b + self.c > self.a) and (self.a + self.c > self.b):
            s = (self.a + self.b + self.c)/2
            area_t = (s*((s-self.a)*(s-self.b)*(s-self.c)))** 0.5 # area calculation
            # Supplying the area as a argument to the superclass polygon
            Polygon.__init__(self, 3, area_t )
            self.area_indicator = 2
        else :
             self.area_indicator=1


    def __str__(self):
        if self.area_indicator==2:
            return "Triangle with area {0}".format(self.area)

        if self.area_indicator==1:
            return "The attributes given do not form a triangle"


pap = Paper(360)
pap = pap+Triangle(3, 4, 5)
pap = pap+Polygon(10, 20)
pap = pap+Polygon(10, 30)
pap = pap+Polygon(5,50)
pap= pap + Polygon(5,52)
pap= pap+Triangle(12,13,5)
pap = pap + Polygon(10,5)
#pap= pap + Polygon(8,25)
#pap = pap + Triangle(5,12,13)
#pap.merge()
#pap.erase()
print(pap)



