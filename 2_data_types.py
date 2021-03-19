# string type
print("string type - text type")
typeOne = "string"
print(typeOne)
print(type(typeOne))
print("")

# specifying the type
print("specifying the type")
typeOne = str("string")
print(typeOne)
print(type(typeOne))
print("---------------------------------------------")


# int type
print("int type - numeric type")
typeTwo = 9
print(typeTwo)
print(type(typeTwo))
print("")

# specifying the type
print("specifying the type")
typeTwo = int(9)
print(typeTwo)
print(type(typeTwo))
print("---------------------------------------------")


# float type
print("float type - numeric type")
typeThree = 9.5
print(typeThree)
print(type(typeThree))
print("")

# specifying the type
print("specifying the type")
typeThree = float(9.5)
print(typeThree)
print(type(typeThree))
print("---------------------------------------------")


# complex type
print("complex type - numeric type")
typeFour = 9j
print(typeFour)
print(type(typeFour))
print("")

# specifying the type
print("specifying the type")
typeFour = complex(9j)
print(typeFour)
print(type(typeFour))
print("---------------------------------------------")


# list type - with strings
print("list type - with strings - sequence type")
typeFive = ["cat", "dog", "pig"]
print(typeFive)
print(type(typeFive))
print("")

# specifying the type
print("specifying the type")
typeFive = list(["cat", "dog", "pig"])
print(typeFive)
print(type(typeFive))
print("---------------------------------------------")


# tuple type - with strings
print("tuple type - with strings - sequence type")
typeSix = ("cat", "dog", "pig")
print(typeSix)
print(type(typeSix))
print("")

# specifying the type
print("specifying the type")
typeSix = tuple(("cat", "dog", "pig"))
print(typeSix)
print(type(typeSix))
print("---------------------------------------------")


# range - from 0 to 5
print("range - from 0 to 5 - sequence type")
typeSeven = range(6)
print(typeSeven)
print(type(typeSeven))
print("")

# specifying the type - same
print("specifying the type - same")
print(typeSeven)
print(type(typeSeven))
print("---------------------------------------------")


# dictionary
print("dictionary -  mapping type")
typeEight = {"ID": 1, "Name": "John"}
print(typeEight)
print(type(typeEight))
print("")

# specifying the type
print("specifying the type")
typeEight = dict({"ID": 1, "Name": "John"})
print(typeEight)
print(type(typeEight))
print("---------------------------------------------")


# set
print("set - set type")
typeNine = {"cat", "dog", "pig"}
print(typeNine)
print(type(typeNine))
print("")

# specifying the type
print("specifying the type")
typeNine = set({"cat", "dog", "pig"})
print(typeNine)
print(type(typeNine))
print("---------------------------------------------")


# frozenset
print("frozenset - set type")
typeTen = frozenset({"cat", "dog", "pig"})
print(typeTen)
print(type(typeTen))
print("")

# specifying the type - same
print("specifying the type - same")
print(typeTen)
print(type(typeTen))
print("---------------------------------------------")


# boolean
print("boolean - boolean type")
typeEleven = True
print(typeEleven)
print(type(typeEleven))
print("")

# specifying the type
print("specifying the type")
typeEleven = bool(5)
print(typeEleven)
print(type(typeEleven))
print("---------------------------------------------")


# bytes
print("bytes - binary types")
typeTwelve = b"TypeTwelve"
print(typeTwelve)
print(type(typeTwelve))
print("")

# specifying the type
print("specifying the type")
typeTwelve = bytes(5)
print(typeTwelve)
print(type(typeTwelve))
print("---------------------------------------------")


# bytearray with 5
print("bytearray with 5 - binary types")
typeThirteen = bytearray(5)
print(typeThirteen)
print(type(typeThirteen))
print("")

# specifying the type - same
print("specifying the type - same")
print(typeThirteen)
print(type(typeThirteen))
print("---------------------------------------------")


# memory view with 5
print("memory view with 5 - binary types")
typeFourteen = memoryview(bytes(5))
print(typeFourteen)
print(type(typeFourteen))
print("")

# specifying the type - same
print("specifying the type - same")
print(typeFourteen)
print(type(typeFourteen))
print("---------------------------------------------")
