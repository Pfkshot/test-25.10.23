"""
В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца.
Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?
"""
import pandas as pd
import random

# Вариант с get_dummies
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst}).head(10)
g = pd.get_dummies(data['whoAmI']).astype(int).head(10)
data.head()

print(data)

print(g)

# Вариант без с get_dummies
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
a = pd.DataFrame({'human': data['whoAmI'] == 'human',
              'robot': data['whoAmI'] == 'robot'}).astype(int).head(10)
data.head()

print(a)

