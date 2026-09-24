class Car:
    EngineType = "Diesel Engine"
    def __init__(self,name,mil,Color):
        print("This is a car class")
        self.name = name
        self.mil = mil
        self.Color = Color


    def Model(self):
        print("The Car Model is ",{self.name})
        

    def mil(self,mil):
        print("The Car milage is ",{self.mil})

    def Color(self,Color):
        print("The Car color is ",{self.Color})

    @classmethod
    def Engine(cls):
       return cls.EngineType
       


c1 = Car("Mahindra",15,"Navy Blue")
c1.EngineType = "EV Engine"


print(c1.name,c1.mil,c1.Color,c1.EngineType)

 # INHERITANCE
class A:
   def Feature1(self):
      print("Feature1 is working")

   def Feature2(self) : 
      print("Feature2 is working")

class B(A):
   def feature3(self):
      print("Feature3 is working")

   def feature4(self):
      print("Feature4 is working")

a1 = A()
a1.Feature1()
b1 = B()
b1.Feature1()
            
      
    