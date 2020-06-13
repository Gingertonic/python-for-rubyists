# Naming Conventions: https://visualgit.readthedocs.io/en/latest/pages/naming_convention.html 

# my_module, my_variable, my_method, my_function
# MY_CONST
# MyClass

# String formatting:
# https://realpython.com/python-string-formatting/#2-new-style-string-formatting-strformat

# Comment

# Variables
zelda = "Twilight Princess Zelda Gaković"

# Methods
def hello_world():
    print("Hello World")


def say_hi_to(name):
    print(f"Greetings, {name}!")


say_hi_to(zelda)

# Conditional
def fizzbuzz(num):
    if (num % 3 == 0 and num % 5 ==0):
        print('FizzBuzz')    
    elif num % 3 == 0: 
        print('Fizz')
    elif num % 5 == 0:
        print('Buzz')
    else:
        print(f"{num} is not divisible by 3 or 5")
        # print("{} is not divisible by {}".format(num, 3))


# Iteration
kitties = ["Rumble", "Sam", "Flora", "Tigerlily"]

for cat in kitties:
    print(cat)