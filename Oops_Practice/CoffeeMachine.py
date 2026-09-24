class MenuItem():
    def __init__(self,name,cost,ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients
       

    def display(self):
        print(f"Name : {self.name}")
        print(f"Cost : {self.cost}")
        print(f"Ingredients : ")
        for ingredient, quantity in self.ingredients.items():
            print(f"{ingredient} : {quantity}")

    

class Menu():
    def __init__(self):
        self.Items = [
            MenuItem( "Cappuccino",
                30,
                {
                    "water": 50,
                    "milk": 100,
                    "coffee": 18
                }),
            MenuItem("Latte",
                25,
                {
                    "water": 50,
                    "milk": 150,
                    "coffee": 15
                }),
            MenuItem("Espresso",
                15,
                {
                    "water": 30,
                    "milk": 0,
                    "coffee": 20
                })
        ]
        
        

    def displayItems(self):
        for item in self.Items:
            print(item.name)

    def find_drink(self,order_name):
        for item in self.Items:
            if item.name == order_name:
                print(f"Your Order {order_name} exists")
                return item
               
              
                      
class CoffeeMachine():
    def __init__(self):
        self.resources = {
            'water' : 1000,
            'milk': 500,
            'coffee': 250
        }       

    def report(self):
        for key, value in self.resources.items():
            print(key, ":",value)

    def is_resource_sufficient(self,drink):
        for ingredient, quantity in drink.ingredients.items():
            if drink.ingredients[ingredient] > self.resources[ingredient]:
                return False 

        if False:
            print('Ingredients are insufficient')   
        else :
            print('The Coffee Machine has sufficient ingredients to make your drink. Please hold on!')    
            return True
    def make_coffee(self,order):
        for ingredient, quantity in order.ingredients.items():
            self.resources[ingredient] = self.resources[ingredient]-order.ingredients[ingredient]

    
class MoneyMachine():
    def __init__(self):
        self.profit = 0
    
    def make_payment(self,drink):
        print(f"Please pay : {drink.cost}")
        print('QR Code displayed....')
        payment_status = input('Payment Successful : (yes/no)?')
        if payment_status == 'yes':
            print('Payment Succeesful')
            return True
        else :
            print('Payment Failed')
            return False
    def profit(self,drink):
        self.profit += drink.cost
        return self.profit

menu = Menu()
drink = menu.find_drink('Cappuccino')
machine = CoffeeMachine()
money = MoneyMachine()
sufficient = machine.is_resource_sufficient(drink)
if sufficient:
    payment_success=money.make_payment(drink)
    if payment_success:
       machine.make_coffee(drink)
    




