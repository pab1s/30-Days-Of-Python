import pandas as pd # importing pandas as pd

# Ejercicio 1
df = pd.read_csv('data/hacker_news.csv')

# Ejercicio 2
print(df.head())

# Ejercicio 3
print(df.tail())

# Ejercicio 4
print(df.columns)

# Ejercicio 5
print(df.shape)
# print(df['Python']) - There's no 'Python' title
# print(df['JavaScript']) - There's no 'JavaScript' title
print(df.describe())