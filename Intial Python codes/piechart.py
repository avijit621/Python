# Import libraries

from matplotlib import pyplot as plt
import numpy as np


class PieChart:
       def __init__(self,input_dict):
                self.input_dict=input_dict

       def __str__(self):
               return "{0}".format(self.input_dict)

       def show(self):
                keys = list(self.input_dict.keys())
                values = list(self.input_dict.values())
                plt.pie(values,labels=keys, autopct='%1.1f%%')
                return plt.show()

       def __add__(self, other):
               for key in other.input_dict:
                       if key in self.input_dict:
                               other.input_dict[key] = other.input_dict[key] + self.input_dict[key]
                       else:
                               pass
               self.input_dict.update(other.input_dict)
               return PieChart(self.input_dict)

       def __sub__(self, other):
               self.input_dict.pop(other)
               return PieChart(self.input_dict)



p = PieChart({"Frogs": 10, "Dog": 25 , 'cat' : 12})
#p.show()
p = p - "Frogs"
print(p)
p.show()
#print(p)
#p.show()
'''
from matplotlib import pyplot as plt
input_dict1 = {"Frogs": 10, "Dog": 25}
input_dict2= {'Frogs': 20, 'Cat': 10}
input_dict1.update(input_dict2)
print (input_dict1)
#keys= list(input_dict.keys())
#values= list(input_dict.values())
#print(keys)
#print(values)
#plt.pie(values,labels=keys)
#plt.show()
'''

