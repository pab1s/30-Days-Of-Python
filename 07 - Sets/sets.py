# sets
it_companies = {'Facebook', 'Google', 'Microsoft',
                'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
print(it_companies.add('Twitter'))
print(it_companies.update({'Xiaomi', 'Samsung'}))
print(it_companies.remove('Samsung'))

# discard() is different from the remove() method,
# because the remove() method will raise an error if
# the specified item does not exist, and the discard()
# method will not.

C = set()
C.update(A)
C.update(B)
print(C)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
print(A.symmetric_difference(B))
del A, B

print(len(age) > len(set(age)))

# Strings is Mutable, it is Unordered collection of items and items in string can be replaced or changed.
# Lists is Mutable, it is Ordered collection of items and items in list can be replaced or changed.
# Set is Mutable, it is Unordered collection of items and items in set cannot be changed or replaced.
# Tuple is Immutable, it is Ordered collection of items and items in tuple cannot be changed or replaced.

print(len('I am a teacher and I love to inspire and teach people.'.split()))
