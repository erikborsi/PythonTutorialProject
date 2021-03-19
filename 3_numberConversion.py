import random as rd

x = 1  # int
y = 2.8  # float
z = 1j  # complex

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)
print("")

# types after conversion:
print(type(a))
print(type(b))
print(type(c))

print("")

print(rd.randrange(1, 10))

randomNumber = rd.randrange(1, 10)
print(randomNumber)

