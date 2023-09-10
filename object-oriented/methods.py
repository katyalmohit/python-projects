class item:
#We use self as a parameter in the methods to access the instance attributes and methods of the class.
    def calculate(self,x,y):
        return x*y

item1 = item()
item1.name = "Phone"
item1.price = 1000
item1.quantity = 3
print(item1.calculate(item1.price, item1.quantity))

item2 = item()
item2.name = "Laptop"
item2.price = 3000
item2.quantity = 2
print(item2.calculate(item2.price, item2.quantity))