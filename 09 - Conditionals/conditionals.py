# Exercise 1
age = int(input('Enter your age: '))

if age < 18:
    print(f'You need {18-age} more years to learn to drive.')
elif age >= 18:
    print('You are old enough to learn to drive.')

# Exercise 2
your_age = int(input('Enter his/her age: '))

if your_age > age:
    print(f'You are {your_age-age} years older than me.')
elif your_age < age:
    print(f'You are {age-your_age} years younger than me.')
else:
    print('You are as old as me.')

# Exercise 3
one = int(input('Enter number one: '))
two = int(input('Enter number two: '))

if one > two:
    print(f'{one} is greater than {two}.')
elif one < two:
    print(f'{two} is greater than {one}.')
else:
    print(f'{two} is equal to {one}.')

# Exercise 4
score = int(input('Enter your score: '))

if 0 <= score <= 49:
    print('Your grade: F.')
elif 50 <= score <= 59:
    print('Your grade: D.')
elif 60 <= score <= 69:
    print('Your grade: C.')
elif 70 <= score <= 89:
    print('Your grade: B.')
else:
    print('Your grade: A.')

# Exercise 5
month = input('Enter the current month: ').capitalize()

if month == 'September' or month == 'October' or month == 'November':
    print('It\'s Autumn.')
elif month == 'December' or month == 'January' or month == 'February':
    print('It\'s Winter.')
elif month == 'March' or month == 'April' or month == 'May':
    print('It\'s Spring.')
elif month == 'June' or month == 'July' or month == 'August':
    print('It\'s Summer.')
else:
    print('You did not enter a month.')

# Exercise 6:
fruits = ['banana', 'orange', 'mango', 'lemon']

fruit = input('Enter a fruit: ')

if fruit in fruits:
    print('That fruit already exists in the list.')
else:
    fruits.append(fruit)

# Exercise 7
person = {
    'first_name': 'Pablo',
    'last_name': 'Olivares',
    'age': 20,
    'city': 'Granada',
    'country': 'Spain',
    'is_married': False,
    'skills': ['C', 'C++', 'Java', 'Ruby', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}

if 'skills' in person:
    print(person['skills'][len(person['skills'])//2])
    if 'Python' in person['skills']:
        print('You have Python as a skill.')
    if ['JavaScript', 'React'] == person['skills']:
        print('You are a front end developer.')
    elif ['Node', 'Python', 'MongoDB'] == person['skills']:
        print('You are a back end developer.')
    elif ['React', 'Node', 'MongoDB'] == person['skills']:
        print('You are a full stack developer.')
    else:
        print('unknown title')

if person['country'] == 'Spain' and person['is_married'] == False:
    print(f'{person["first_name"]} {person["last_name"]} lives in {person["country"]}. He is not married.')