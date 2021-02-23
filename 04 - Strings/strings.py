# Practicing with strings
greeting = 'Thirty ' + 'days ' + 'of ' + 'Python'
company = 'Coding ' + 'For ' + 'All'
print(greeting, company)

print(company)
print(len(company))
print(company.upper())
print(company.lower())
print(company.capitalize())
print(company.title())
print(company.swapcase())
print(company.lstrip('Coding'))
print(company.find('Coding'))
print(company.replace('Coding', 'Practicing'))
print(company.split(' '))
print("Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon".split(', '))

print(company[0])
print(company[10])
print("".join(c[0] for c in company.split()))
print(company.index('C'))
print(company.index('F'))
print(company.rfind('l'))

print('You cannot end a sentence with because because because is a conjunction'.index('because'))
print('You cannot end a sentence with because because because is a conjunction'.rindex('because because because'))
print('You cannot end a sentence with because because because is a conjunction'.find('because'))
print('You cannot end a sentence with because because because is a conjunction'[31:54])

print(company.find('Coding') == 0)
print(company.split()[-1] == 'Coding')
print(' '.join('   Coding For All      '.split()))

print('30DaysOfPython'.isidentifier())
print('thirty_days_of_python'.isidentifier())

web_tech = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
print(' # '.join(web_tech))

print('I am enjoying this challenge.\nI just wonder what is next.')
print('Name\tAge\tCountry\nPablo\t20\tSpain')

radius = 10
area = 3.14 * radius ** 2
print(f'The area of a cricle with radius {radius} is {area:.0f} meters square.')

a = 8
b = 6
print(f'{a} + {b} = {a +b}')
print(f'{a} - {b} = {a - b}')
print(f'{a} * {b} = {a * b}')
print(f'{a} / {b} = {a / b:.2f}')
print(f'{a} % {b} = {a % b}')
print(f'{a} // {b} = {a // b}')
print(f'{a} ** {b} = {a ** b}')