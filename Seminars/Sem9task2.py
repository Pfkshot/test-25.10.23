'''
Дан файл california_housing_train.csv.
Найти максимальное значение переменной "households" в зоне минимального значения переменной
 min_population и сохраните это значение в переменную max_households_in_min_population.
Используйте модуль pandas.
'''
from pandas import read_csv

data = read_csv('california_housing_test.csv')

min_population = data['population'].min()

max_households_in_min_population = data[data['population'] == min_population]['households'].max()

print(max_households_in_min_population)
