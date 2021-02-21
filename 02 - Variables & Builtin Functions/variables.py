# Day 2: 30 Days of python programming

# Declaring some variables
first_name = 'Pablo'
last_name = 'Olivares'
full_name = 'Pablo Olivares'
country = 'Spain'
city = 'Granada'
age = 20
year = 2021
is_married = False
is_true = True
is_light_on = False

# Declaring some variables in one line
first_name, last_name, country, age, is_married = 'Pablo', 'Olivares', 'Granada', 20, False

# Printing the info
print('First name: ', first_name)
print('Last name: ', last_name)
print('Age: ', age)
print('Is he married?', is_married)

# Checking the data type
print(type(first_name))
print(type(last_name))
print(type(full_name))
print(type(country))
print(type(city))
print(type(age))
print(type(year))
print(type(is_married))
print(type(is_true))
print(type(is_light_on))

# Using and comparing lengths
print(len(last_name))
print(len(first_name) == len(last_name))
print(len(first_name) > len(last_name))
print(len(first_name) < len(last_name))

# Operations with variables
num_one, num_two = 5, 4
_total = num_one + num_two
_diff = num_one - num_two
_product = num_one * num_two
_division = num_one / num_two
_remainder = num_one % num_two
_exp = num_one ** num_two
_floor_division = num_one // num_two

print(num_one, num_two, _total, _diff, _product,
      _division, _remainder, _exp, _floor_division)

# Area and circumference of a circle
radius = float(input('Introduce the radius: '))
area_of_circle = 3.1416 * radius ** 2
circum_of_circle = 3.1416 * 2 * radius
print('Area: ',area_of_circle , 'Circumference: ', circum_of_circle)

# Introduce information
first_name = input('Introduce your first name: ')
last_name = input('Introduce your last name: ')
country = input('Introduce your country: ')
age = input('Introduce your age: ')

# help()
help('keywords')