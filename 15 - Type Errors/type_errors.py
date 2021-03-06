# Exercises

# SyntaxError
# print 'Hello World!' # Missing parenthesis

# NameError
# print(age) # age does not exist

# IndexError
numbers = [1, 2, 3, 4, 5]
# numbers[5] # numbers has no 6th element, index goes from 0 to 4

# ModuleNotFoundError
# import maths # This module does not exist, the module is 'math'

# AttributeError
import math
# math.PI # The attribute 'PI' does not exist in 'math', 'pi' is the attribute to use

# KeyError
users = {'name':'Pablo', 'age':20, 'country':'Spain'}
# users['county'] # 'county' is not a key in users, the key is 'country'

# TypeError
# 2 + '3' # You cannot add an int and a string

# ImportError
# from math import power # TypeError: power is not a fuction in math to import, the function is 'pow()'
# int('12a') # ValueError: you cannot convert '12a' into an int
 1/0 # ZeroDivisionError: we cannot divide a number by zero