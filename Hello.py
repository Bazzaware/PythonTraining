msg = "Hello, World"
print(msg)
print(msg.lower)
print(len(msg))
print(msg[2:5])
print(msg.replace("H","J"))
print(msg.split(","))

x = "awesome"
print("Python is " + x)

x = "Python is "
y = "awesome"
z =  x + y
print(z)

x = 3    # int
y = 2.8  # float
z = 1j   # complex

dir(x) # Shows all methods available on object

x.to_byte(10,'big')


print(type(x))
print(type(y))
print(type(z))

x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2


# A list is a collection which is ordered and changeable. In Python lists are written with square brackets.
thislist = ["apple", "banana", "cherry"]
print(thislist)
thislist[1] = "Blackcurant"
print(thislist)

# A tuple is a collection which is ordered and unchangeable. In Python tuples are written with round brackets.
thistuple = ("apple", "banana", "cherry")
# thistuple[1] = "blackcurrant" This will cause an error
# The values will remain the same:
print(thistuple)

# A set is a collection which is unordered and unindexed. In Python sets are written with curly brackets.
thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x)

a = 33
b = 200
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# The and keyword is a logical operator, and is used to combine conditional statements:
c = 500
if a < b and c > a:
  print("Both conditions are True")

# The or keyword is a logical operator, and is used to combine conditional statements:
if a < b or a > c:
  print("At least one of the conditions are True")

# Print i as long as i is less than 6: 
i = 1
while i < 6:
  print(i)
  i += 1


def my_function():
  print("Hello from a function")

my_function()

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

# The power of lambda is better shown when you use them as an anonymous function inside another function.
# Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number:
def myFunc(n):
    return lambda a: a * n

myDoubler = myFunc(2)
print(myDoubler(11))

myTripler = myFunc(3)
print(myTripler(22))

class MyClass:
  x = 5
p1 = MyClass()
print(p1.x)

class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()