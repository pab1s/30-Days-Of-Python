# Exercise
names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries, es, ru = names
print(nordic_countries, es, ru)

# Some practice
try:
    print(4 + '2')
except TypeError:
    print('You cannot add a string and an integer.')
else:
    print('Everything went OK!')
finally:
    print('This is the end of this sequence, no matter everything went OK or not.')

countries = ['Spain', 'Italy', 'France', 'Germany', 'United Kingdom']
capitals = ['Madrid', 'Rome', 'Paris', 'Berlin', 'London']
info = []
for country, capital in zip(countries, capitals):
    info.append({'Country':country, 'Capital':capital})
print(info)

for index, i in enumerate(countries):
    print('hi')
    if i == 'Germany':
        print(f'The country {i} has been found at index {index}')