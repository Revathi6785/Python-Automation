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
    