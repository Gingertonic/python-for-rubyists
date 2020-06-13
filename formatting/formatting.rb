# my_variable, my_method
# MyModule
# MyClass
# MY_CONSTANT

# Comment





# Variables
zelda = "Twilight Princess Zelda Gaković"

# Methods
def hello_world
    puts "Hello World"
end

def say_hi_to(name)
    puts "Greetings, #{name}!"
end

say_hi_to zelda

# Conditional
def fizzbuzz(num)
    if num % 3 == 0 && num % 5 == 0
        puts "FizzBuzz"
    elsif num % 3 == 0
        puts "Fizz"
    elsif num % 5 == 0
        puts "Buzz"
    else
        puts "#{num} is not divisible by 3 or 5"
    end
end

# Iteration
kitties = ["Rumble", "Sam", "Flora", "Tigerlily"]

kitties.each{|cat| puts cat}
