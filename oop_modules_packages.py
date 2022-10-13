# Example Use Case - Lucky Draw
# import random

# from random import random

# print(random.random())
# print(random())

# Each time it's run generates a random number - 0-1
# calculate DOB or year of birth
#
# import math
#
# number = 23.66
# # number 1.50 above to round up 2
# # number 1.49 less round down to  1
# print(math.ceil(number))
# print(math.floor(number))
#

# import os, sys
#
# print(os.cpu_count())  # Will display the no. of CPU
# print(sys.path)

# import datetime
# print(datetime.date.today())  # Displays today's date based on OS

# Don't Repeat Yourself (DRY)
# Reusable - Saves time - save money
# Syntax def name():

# First Iteration - Greet User
# def greeting():
#     print("Hello Dear")
#     # pass  # Keyword pass - It is a null statement i.e. it doesn't return anything
#
# greeting()

# Second Iteration - Greet User by their name
# Create a function that takes an argument - the name
# def greet_user(name):
#     print("Hello Dear " + name)
#
#
# greet_user("Sparta")

# Third Iteration - Taking Int as argument
# def add(value1, value2):
#     print(value1 + value2)
#
#
# add(2, 3)


# Fourth Iteration - Using return keyword
def add(value1, value2):
    return value1 + value2


# Return statement only returns value, doesn't print anything
print(add(2, 3))
