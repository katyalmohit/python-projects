def cube(num):
    print('hello') #this will be printed
    return num*num*num
    print('hello again') #statements after return statement will not be executed in functions
num = int(input("Enter number: "))
cube = cube(num)
print(cube)