# Import libraries

from matplotlib import pyplot as plt
import numpy as np

class PieChart:
       def __init__(self,input_dict):
                self.input_dict=input_dict # A dictionary to store the values
                for i in list(self.input_dict.values()): # Exception handling to check the
                     if i < 0 :                          # whether the values are positive or not
                       try:
                         raise Exception('Value should be a positive number')
                       except Exception as inst:
                               print(type(inst))
                               print(inst)
                     else:
                        pass
                for i in list(self.input_dict.keys()):
                     if isinstance(i,str) is False : # Exception handling for
                       try:                          # Checking to see the key values are strings or not
                         raise Exception('Label should be a string')
                       except Exception as inst:
                               print(type(inst))
                               print(inst)
                     else:
                        pass 
                     
       def __str__(self):
               return "{0}".format(self.input_dict)

       def show(self): # Show function to show the plot
                keys = list(self.input_dict.keys())
                values = list(self.input_dict.values())
                plt.pie(values,labels=keys, autopct='%1.1f%%')
                return plt.show()

       def __add__(self, other): # addition overloaded to add new keys and values
               for key in other.input_dict:
                       if key in self.input_dict:
                           other.input_dict[key] = other.input_dict[key] + self.input_dict[key]
                       else:
                               pass
               self.input_dict.update(other.input_dict) # updating the diict values with new values
               return PieChart(self.input_dict)

       def __sub__(self, other):
           # Pooping out the values corresponding to the key to be erased
               self.input_dict.pop(other)
               return PieChart(self.input_dict)


#p=PieChart({5: 1})
p = PieChart({"Frogs": 10, "Dog": 25 , 'cat' : 12})
#p = p + PieChart({'Lions': 25, "Sheep" : 22})
#p.show()
#p = p - "Sheep"
#print(p)
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

