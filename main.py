from math import *

# This is code that I wrote / played with when taking a freecodecamp Python course to refresh my memory

# A comment shortcut in Pycharm is control + /

# Variables
# Use underscores instead of Camelcase
my_cats_name = "Orby"
my_cats_age = 4
orby_likes_water = False
orby_like_cheese = True
orby_can_run = 10.5

# Strings
print("My cats name is " + my_cats_name)
# String concatenate using f-strings
print(f'My cats name is {my_cats_name} and she is {my_cats_age} years old. She can run {orby_can_run} miles per hour')
# \n = new line
# \ is an escape character
# Printing a variable
print(my_cats_age)
# Turning Orby's name into all uppercase
print(my_cats_name.upper())
# Checking to see if
print(my_cats_name.isupper())
# Converting the variable to upper then checking to see if its upper
print(my_cats_name.upper().isupper())
# Getting the length of the string
print(len(my_cats_name))
# Getting the first letter of the variable name
print(my_cats_name[0])
# Indexes start with zero
print(my_cats_name.index("y"))
print(my_cats_name.replace("rby", "RBY"))

# Numbers
# PEMDAS order
print(2*4)
# Mod
print(10 %3)
my_num = 1
print(my_num + 1)
print(str(my_num))
# Common math functions
# Absolute
print(abs(my_num))
# Power
print(pow(2, 2))
# Max (also has min)
print(max(2, 10))
# Round (rounds stuff)
print(round(3.2))
# Floor
print(floor(3.7))
# Ceil
print(ceil(2.2))
# SQRT
print(sqrt(5))
