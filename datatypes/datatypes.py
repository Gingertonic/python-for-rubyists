# How to find what type a piece of data is
# type(thing)

type("banana") #=> <class 'string'>

type(True) #=> <class 'bool'>
type(False) #=> <class 'bool'>

type(42) #=> <class 'int'>
type(3.14) #=> <class 'float'>
type(6+4j) #=> <class 'complex'>

type((7,4,8)) #=> <class 'tuple'>
# ordered, immutable

type(["north", "south", "east", "west"]) #=> <class 'list'>
# ordered, mutable

type({ "name": "Zelda", "age": 2 }) #=> <class 'dict'>
type({ 1: "Zelda", 3: 2 }) #=> <class 'dict'>
# unordered, key:value pairs

type({'hi', 'hola', 'hi', 'ciao'}) #=> <class 'set'>
# unordered, unique values only


# Accessing data in collections
my_list = ["first", "second", "third"]
my_list[1]

tup = ("cat", "dog", "bun")
tup[1]

my_dict = { "name": "Zelda", "age": 2 }
my_dict["name"]

my_set = {'hi', 'hola', 'hi', 'ciao'}
for greeting in my_set:
    print(greeting)


