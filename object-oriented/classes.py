class item:
    pass

item1 = item()
item1.name = "Phone"
item1.price = 1000
item1.quantity = 3
print(type(item1)) #printing type of item1
print(type(item1.name))
print(type(item1.price))
print(type(item1.quantity))

item2 = item()
item2.name = "Laptop"
item2.price = 3000
item2.quantity = 2