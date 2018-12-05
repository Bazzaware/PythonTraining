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

