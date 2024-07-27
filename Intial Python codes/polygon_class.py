class Polygon:
  def __init__(self, numsides, area):
     self.num_sides = numsides
     self.area = area

     if self.area < 0:
         try:
          raise Exception("Polygon should have positive area")
         except Exception as inst:
                 print(type(inst))
                 print(inst)
     elif self.num_sides < 3:
         try:
           raise Exception("Number of sides should be at least 3 ")
         except Exception as inst:
              print(type(inst))
              print(inst)
     else:
          pass
  def __str__(self):
     return"Polygon with sides {0} and area {1}".format(self.num_sides, self.area)








p1 = Polygon(10, 25)
print(p1)
