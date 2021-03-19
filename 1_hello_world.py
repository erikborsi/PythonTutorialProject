print('Hello World!')

x = 9
y = 9.0
z = "string"

print(type(x))
print(type(y))
print(type(z))

globalVariable = "something"


def myFunction():
    global globalVariable
    globalVariable = "global"
    print("This is a string " + z)


myFunction()
print(globalVariable)

# assign multiple values
x, y, z = "cat", "dog", "pig"
print(x)
print(y)
print(z)

# assign same value to different varibles
x, y, z = "cat"
print(x)
print(y)
print(z)

# create a collection (list) and extract values
fruits = ["cat", "dog", "pig"]
x, y, z = fruits
print(type(fruits))
print(x)
print(y)
print(z)
