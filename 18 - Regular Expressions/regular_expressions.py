import re
from collections import Counter
import functools

# Exercise 1
def most_frequent_words(s):
    words = re.findall(r'\w+', s.lower())
    print (Counter(words))
    return Counter(words)

paragraph = 'I love teaching. If you do not love teaching what else can you love. I love Python if you do not love something which can give you all the capabilities to develop an application what else can you love.'
most_frequent_words(paragraph)

# Exercise 2
def get_numbers(s):
    numbers = re.findall(r'-?\d', s)
    numbers = [int(n) for n in numbers]
    numbers.sort()
    distance = numbers[-1] - numbers[0]
    print(numbers)
    print(distance)
    return numbers

axis = 'The position of some particles on the horizontal x-axis -12, -4, -3 and -1 in the negative direction, 0 at origin, 4 and 8 in the positive direction.'
get_numbers(axis)

# Exercise 3
def is_valid_variable(s):
    lst = re.findall(r'^[a-zA-Z_$][a-zA-Z_$0-9]*$', s)
    print(not (lst == []))
    return not (lst == [])

is_valid_variable('first_name') # True
is_valid_variable('first-name') # False
is_valid_variable('1first_name') # False
is_valid_variable('firstname') # True

# Exercise 4
def clean_text(s):
    s = re.sub(r"[\$\&\%-()\"#/@;:<>{}=~|.?!,]", "", s)
    print(s)
    return s

sentence = '''%I $am@% a %tea@cher%, &and& I lo%#ve %tea@ching%;. There $is nothing; &as& mo@re rewarding as educa@ting &and& @emp%o@wering peo@ple. ;I found tea@ching m%o@re interesting tha@n any other %jo@bs. %Do@es thi%s mo@tivate yo@u to be a tea@cher!?'''
clean_text(sentence)