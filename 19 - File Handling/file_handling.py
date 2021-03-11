import os
import re
import json
import csv
from collections import Counter

# Exercise 1


def n_words_lines(s):
    file = open(s)
    text = file.read()
    lines = len(file.readlines())
    words = len(text.split())
    file.close()
    return words, lines


print(n_words_lines('data/obama_speech.txt'))
print(n_words_lines('data/michelle_obama_speech.txt'))
print(n_words_lines('data/donald_speech.txt'))
print(n_words_lines('data/melina_trump_speech.txt'))

# Exercise 2


def most_spoken_languages(s, n):
    file = open(s)
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


def most_populated_countries(s, n):
    file = open(s)
    countries = json.loads(file.read())
    population_ranking = dict()
    top_population = list()

    for country in countries:
        population_ranking[country["name"]] = country["population"]

    for i in range(n):
        maximum = max(population_ranking, key=population_ranking.get)
        top_population.append(
            {'country': population_ranking[maximum], 'population': maximum})
        population_ranking.pop(maximum)
    file.close()
    return top_population


print(most_populated_countries('./data/countries_data.json', 10))

# Exercise 4


def extract_incoming_mails(s):
    file = open(s)
    countFromEmail = 0
    unique_emails = set()
    for line in file:
        if re.findall('^From:.+@([^\.]*)\.', line):
            countFromEmail += 1
            line = line.replace("From:", "")
            line = line.strip()
            unique_emails.add(line)
    return unique_emails


print(extract_incoming_mails('data/email_exchanges_big.txt'))

# Exercise 5


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


print(most_frequent_words('data/romeo_and_juliet.txt', 10, True))

# Exercise 6
print(most_frequent_words('data/obama_speech.txt', 10, True))
print(most_frequent_words('data/michelle_obama_speech.txt', 10, True))
print(most_frequent_words('data/donald_speech.txt', 10, True))
print(most_frequent_words('data/melina_trump_speech.txt', 10, True))

# Exercise 7


def remove_items(test_list, item):
    res = [i for i in test_list if i != item]
    return res


def clean_text(s):
    s = re.sub(r"[\$\&\%-()\"#/@;:<>{}=~|.?!,]", "", s)
    return s


def remove_support_words(s):
    support_words = ['the', 'and', 'to', 'of', 'a', 'in', 'for', 'that']
    stop_words = ['i', 'me', 'us', 'my', 'myself', 'we', 'our', 'ours', 'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your', 'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she', "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself', 'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who', 'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having', 'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if', 'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for', 'with', 'about', 'against', 'between', 'into', 'through', 'during', 'before', 'after', 'above', 'below', 'to', 'from', 'up',
                  'down', 'in', 'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once', 'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both', 'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't', 'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now', 'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn', "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't", 'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn', "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't", 'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won', "won't", 'wouldn', "wouldn't"]
    words = re.findall(r'\w+', s.lower())
    for sw in support_words:
        if sw in words:
            words = remove_items(words, sw)
    for sw in stop_words:
        if sw in words:
            words = remove_items(words, sw)
    return ' '.join(words)


def check_text_similarity(s1, s2):
    f1 = open(s1)
    f2 = open(s2)
    text1 = f1.read()
    text2 = f2.read()
    text1 = clean_text(text1)
    text2 = clean_text(text2)
    text1 = remove_support_words(text1)
    text2 = remove_support_words(text2)
    text1 = most_frequent_words(text1, 15, False)
    text2 = most_frequent_words(text2, 15, False)

    for word in text1:
        if word in text2:
            print(word, 'is a word which usually appears in both texts.')
    f1.close()
    f2.close()
    return text1, text2


print(check_text_similarity(
    'data/michelle_obama_speech.txt', 'data/melina_trump_speech.txt'))

# Exercise 8
print(most_frequent_words('data/romeo_and_juliet.txt', 10, True))

# Exercise 9


def python_in_csv(s):
    python_count = 0
    js_count = 0
    java_count = 0

    with open(s) as f:
        csv_reader = csv.reader(f, delimiter=',')
        for row in csv_reader:
            for sentence in row:
                if 'Python' in sentence or 'python' in sentence:
                    python_count += 1
                if 'Javascript' in sentence or 'javascript' in sentence or 'JavaScript in sentence':
                    js_count += 1
                if 'Java' in sentence or 'java' in sentence:
                    java_count += 1
    return python_count, js_count, java_count


print(python_in_csv('data/hacker_news.csv'))
