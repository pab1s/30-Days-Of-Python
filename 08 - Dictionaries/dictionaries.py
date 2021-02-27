# Exercises
empty_dict = dict()
dog = {
    'name': 'Rex',
    'color': 'brown',
    'breed': 'pug',
    'legs': 4,
    'age': 4
}
print(dog)

student = {
    'first_name': 'Pablo',
    'last_name': 'Olivares',
    'age': 20,
    'city': 'Granada',
    'country': 'Spain',
    'is_married': True,
    'skills': ['C', 'C++', 'Java', 'Ruby', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
print(len(student))
print(student['skills'])
print(type(student['skills']))
student['skills'].extend(['Bash', 'Assembly'])
print(student['skills'])
print(student.keys())
print(student.values())
print(student.items())
student.pop('is_married')

del dog