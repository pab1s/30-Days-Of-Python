age = 20
height = 1.85
i = 1 + 2j

# Script to calculate the area of a traingle given the base and height
base = float(input('Enter base: '))
height = float(input('Enter height: '))
area = 0.5 * base * height
print('The area of the triangle is ', area)

# Script to calculate the perimeter of a traingle given the base and height
a = int(input('Enter side a: '))
b = int(input('Enter side b: '))
c = int(input('Enter side c: '))
perimeter = a + b + c
print('The perimeter of the triangle is ', perimeter)

# Script to calculate the area and perimeter of a rectangle
length = float(input('Enter length: '))
width = float(input('Enter width: '))
area = length * width
perimeter = 2*length + 2*width
print('The area of the rectangle is ', area)
print('The perimeter of the rectangle is ', perimeter)

# Calculate the area and circumference of a circle
pi = 3.14
r = float(input('Enter radius: '))
area = pi * r * r
c = 2 * pi * r
print('The area of the circle is ', area, ' and the circumference is ', c)

# Calculate the slope of y = 2x - 2
x_1 = 0
y_1 = 2 * x_1 - 2
y_2 = 0
x_2 = (y_2 + 2) / 2
slope = (y_2 - y_1) / (x_2 - x_1)
print('The slope is ', slope)
print('x-intercept: ', y_1)
print('y-intercept: ', x_2)

# Find the slope of (2,2) and (6,10)
m = (10 - 2) / (6 - 2)
print('Slope: ', m)

# Comparing slopes
print(slope > m)
print(slope < m)
print(slope == m)

# Comparing 'python' and 'jargon'
p = len('python')
j = len('jargon')
print('python' == 'jargon')

# See if 'on' is in both strings and other comparisons
print('on' in 'python' and 'on' in 'jargon')
print('jargon' in 'I hope this course is not full of jargon.')
print('on' not in 'dragon' and 'on' not in 'python')
print(str(float(len('python'))))

# See if a number is even and other comparisons
number = 3
print(number%2 == 0)
print(7//3 == int(2.7))
print('10' == 10)
print(int('9.8') == 10)

# Script hours and rate per hour
hours = int(input('Enter hours: '))
rate = int(input('Enter rate per hour: '))
print('Your weekly earning is ', rate * hours)

# Script Years to seconds
years = int(input('Enter number of years you have lived: '))
print('You have lived for ', years*365*24*60*60, ' seconds.')

# Print the values
print('1 1 1 1 1')
print('2 1 2 4 8')
print('3 1 3 9 27')
print('4 1 4 16 64')
print('5 1 5 25 125')