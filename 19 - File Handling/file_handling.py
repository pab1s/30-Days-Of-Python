import os
import re
import json
# Exercise 1
def n_words_lines(s):
    file = open(s)
    text = file.read()
    lines = len(file.readlines())
    words = len(text.split())
    file.close()
    print (words, lines)
    return words, lines

n_words_lines('data/obama_speech.txt')
n_words_lines('data/michelle_obama_speech.txt')
n_words_lines('data/donald_speech.txt')
n_words_lines('data/melina_trump_speech.txt')

# Exercise 2
def most_spoken_languages(s,n):
    file =open(s)
    countries = json.loads(file.read())
    lang_ranking = dict()
    top_langs = list()

    for country in countries:
        for lang in country["languages"]:
            if lang in lang_ranking:
                lang_ranking[lang] += country["population"]
            else:
                lang_ranking[lang] = country["population"]
    for i in range(n):
        maximum = max(lang_ranking, key=lang_ranking.get)
        top_langs.append((lang_ranking[maximum], maximum))
        lang_ranking.pop(maximum)
    file.close()
    return top_langs

print(most_spoken_languages('./data/countries_data.json', 10))

# Exercise 3
def most_populated_countries(s,n):
    file =open(s)
    countries = json.loads(file.read())
    population_ranking = dict()
    top_population = list()

    for country in countries:
        population_ranking[country["name"]] = country["population"]

    for i in range(n):
        maximum = max(population_ranking, key=population_ranking.get)
        top_population.append({'country':population_ranking[maximum], 'population':maximum})
        population_ranking.pop(maximum)

    return top_population

print(most_populated_countries('./data/countries_data.json', 10))

# Exercise 4
def extract_incoming_mails():
    