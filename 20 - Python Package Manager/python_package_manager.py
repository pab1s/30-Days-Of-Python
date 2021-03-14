import webbrowser
import requests
import re
from collections import Counter
import os

# Exercise 1
def most_frequent_words(s, n, b):
    if b == True:
        file = open(s)
        text = file.read()
    else:
        text = s
    words = re.findall(r'\w+', text.lower())
    words = [(k, v) for k, v in dict(Counter(words)).items()]
    words.sort(key=lambda tup: tup[1])
    words.reverse()
    if b == True:
        file.close()
    return words[:n]

Romeo_and_juliet = 'http://www.gutenberg.org/files/1112/1112.txt'
response = requests.get(Romeo_and_juliet)
print(most_frequent_words(response.text, 10, False))

# Exercise 2
def get_numbers(s):
    numbers = []
    for item in s:
        for subitem in item.split():
            if(subitem.isdigit()):
                numbers.append(subitem)
    numbers = [int(n) for n in numbers]
    return numbers

def average_weight_cats(cats):
    weight_strs = []
    average_weight = 0
    for cat in cats:
        weight_strs.append(cat['weight']['metric'])
    average_weight = sum(get_numbers(weight_strs)) / (len(weight_strs)*2) 
    return average_weight   

cats_api = 'https://api.thecatapi.com/v1/breeds'
response = requests.get(cats_api)
cats = response.json()
print(average_weight_cats(cats))

# Exercise 3
def largest_countries(countries):
    size_ranking = dict()
    top_size = list()

    for country in countries:
        size_ranking[country["name"]] = country["area"]
    size_ranking = {k: v for k, v in size_ranking.items() if v}

    for i in range(10):
        maximum = max(size_ranking, key=size_ranking.get)
        top_size.append((size_ranking[maximum], maximum))
        size_ranking.pop(maximum)

    return top_size

url = 'https://restcountries.eu/rest/v2/all'
response = requests.get(url)
countries = response.json()
print(largest_countries(countries))

# Exercise 4 - Read