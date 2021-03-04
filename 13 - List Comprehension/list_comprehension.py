# Exercise 1
numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
num_list = [i for i in numbers if i <= 0]
print(num_list)

# Exercise 2
list_of_lists =[[[1, 2, 3]], [[4, 5, 6]], [[7, 8, 9]]]
flattened_list_of_lists = [n for row in list_of_lists for ele in row for n in ele]
print(flattened_list_of_lists)

# Exercise 3
list_of_tuples = [(i, 1, i * i, i**3, i**4, i**5) for i in range(11)]
print(list_of_tuples)

# Exercise 4
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
flattened_countries_list = [c.upper() for r in countries for group in r for c in group]
print(flattened_countries_list)

# Exercise 5
countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
list_of_dict = [{'country':k.upper(), 'city':v.upper()} for row in countries for k,v in row]
print(list_of_dict)

# Exercise 6
names = [[('Pablo', 'Olivares')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
concatenated_strings = [' '.join(name) for lst in names for name in lst]
print(concatenated_strings)

# Exercise 7
slope = lambda a,b: a
print(slope(3,2))       # y = 3x + 2