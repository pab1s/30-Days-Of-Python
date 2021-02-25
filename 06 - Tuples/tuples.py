# Exercises
siblings = tuple()
brothers = ('John',)
sisters = ('Marta',)
siblings = brothers + sisters
print(siblings)
print(len(siblings))
parents = ('Frank', 'Maria')
family_members = siblings + parents
print(family_members[0:2], family_members[-2:])

fruits = ('banana', 'orange', 'mango', 'lemon')
vegetables = ('Tomato', 'Potato', 'Cabbage','Onion', 'Carrot')
animal_products = ('meat', 'eggs', 'milk', 'fish')
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
result = list()
result.append(food_stuff_tp[len(food_stuff_tp)//2])
result.append(food_stuff_tp[~len(food_stuff_tp)//2])
print(tuple(dict.fromkeys(result)))
print(food_stuff_lt[-3:])
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)