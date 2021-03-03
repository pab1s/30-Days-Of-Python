# Exercise 1
from random import randint, shuffle
from string import ascii_letters, digits


def random_user_id():
    letters = ''.join(set(ascii_letters.lower()))
    alphanumeric = [letters, digits]
    id = str()

    for i in range(6):
        k = randint(0, 1)
        id += alphanumeric[k][randint(0, len(alphanumeric[k])-1)]

    return id


print(random_user_id())

# Exercise 2
def user_id_gen_by_user():
    letters = ''.join(set(ascii_letters.lower()))
    alphanumeric = [letters, digits]
    id_list = list()
    id = str()

    num_char = int(input('Enter the number of character\'s per ID: '))
    num_id = int(input('Enter the number of ID\'s to create: '))
    for j in range(num_id):
        for i in range(num_char):
            k = randint(0, 1)
            id += alphanumeric[k][randint(0, len(alphanumeric[k])-1)]
        
        id_list.append(id)
        id = ""
    return id_list


print(user_id_gen_by_user())

# Exercise 3
def rgb_color_gen():
    return f'rgb({randint(0,255)},{randint(0,255)},{randint(0,255)})'

print(rgb_color_gen())

# Exercises 4, 5 & 6
def list_of_colors(format, n):
    lst = list()

    if format == 'rgb':
        for i in range(n):
            lst.append(rgb_color_gen())
    elif format == 'hexa':
        for i in range(n):
            lst.append(str('#' + hex(randint(0, 255))))
    return lst

print(list_of_colors('hexa', 4))

# Exercise 7
def shuffle_list(lst):
    shuffle(lst)
    return lst

print(shuffle_list(['A','B','C','C','D']))

# Exercise 8
def randint_array():
    array = ""

    while len(array) < 7:
        array += str(randint(0,9))
        array = ''.join(set(array))
    return array

print(randint_array())