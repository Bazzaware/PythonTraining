# Exercse 0
print("Hello World")
1 + 2 + 3 + 4

help(range)

x = 3.2

dir(x)

# Exercise 01

stones = 16
pounds =  10
kg = (stones * 14 + pounds) / 2.2
print(kg)

# Run to the moon
total = 0
days = 0
distance_per_day = 10
distance_to_the_moon = 238900
total_run = 0

while total_run < distance_to_the_moon:
    total_run = total_run + distance_per_day
    days = days + 1
    distance_per_day = distance_per_day * 1.1 

print(days)
print(round(total_run,2))
# help(round)

# String

name = input("What is your name? ")
age = input("What is your age?")
dob = input("What is your Date of Birth?")

greeting = "Your name is {}.\nYour age is {}\nand your DOB is {}"
print(greeting.format(name,age,dob))

# Exercise 3
# Lists
my_list = []
len(my_list)

my_list.append("fish")
my_list.append("dog")
my_list.append("cat")
my_list.append("bird")
my_list.append("snake")
len(my_list)
my_list[-1] # last entry
my_list[2] = "bacon" # change entry in position 2

for entry in my_list :
    print(entry)

while len(my_list) > 0:
    value = my_list.pop() # will give you the last item and then remove it from the list
    print(value)
    
print(my_list)

"cat" in my_list # returns true or false

if "dog" in my_list :
    print("you have a dog") # Used in an if 

string = "This is a long string that we are going to look for words in."

"long" in string
"missing" in string

#Global variables normally in UPPER CASE

# Exercise 3 Functions
import math
math.sin(90)

def name(argument1, argument2):
    result = argument1 + argument2
    return result

name("Bazza","Test") # BazzaTest
name("Bazza",str(1)) # Bazza1
try:
    name("Bazza",1) # TypeError: Can't convert 'int' object to str implicitly
except expression as e:
    print(" Error type :" type(e))
    print(str(e))

name(1,10) # 11


# Exercise 4 Exceptions

try:
    foo # this does not exist
except Exception as e :
    print(type(e))
    print(str(e))
    raise

try:
    with open("foo.txt") as handle:
        data = handle.read()
except Exception as e :
    print(type(e))



try:
    with open("foo.txt") as handle:
        data = handle.detach()
        data = handle.read()
except FileNotFoundError:
    print("Missing foo.txt")
    data = ""
except Exception as e :
    print(type(e))


# Exercise 5 Classes

class Person:
    def say_hello(self):
        print("Hello")
me = Person()

me.say_hello()

class Person2:
    greeting = "Hello my name is {}"
    def __init__(self,name):
        print("Setting self.name to", name)
        self.name = name
    def say_hello(self):
        print(self.greeting.format(self.name))

michael = Person2("Michael")
jane = Person2("Jane")
bazza = Person2("Bazza")
jane.say_hello()
michael.say_hello()
bazza.say_hello()

class Location:
    def __init__(self,name,lon,lat):
        self.name = name
        self.lon = lon
        self.lat  = lat

here = Location("Southampton",100, 3000)
Location()

# Exercise 6 

class Thing:
    def __init__(self, number):
        if not isinstance(number, (float, int)):
           raise TypeError("number should be a number")
        self._number = number

    def add(self, another_number):
        return self.number + another_number

test= Thing(42)

class ADifferentThing:
    @property
    def attribute(self):
        print("Attribute looked up")
        return 3
thing = ADifferentThing()
thing.attribute
thing.attribute = 4


class Thing:
    def __init__(self, number):
        if not isinstance(number, (float, int)):
           raise TypeError("number should be a number")
        self._number = number

    @property
    def number(self):
        return self._number

    def add(self, another_number):
        return self.number + another_number

