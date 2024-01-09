'''
Дан файл california_housing_train.csv. Определить среднюю стоимость дома ,
где количество людей от 0 до 500 (population) и сохранить ее в переменную avg.
Используйте модуль pandas.
'''

from pandas import read_csv

data = read_csv('california_housing_test.csv')

avg = data[(data['population'] < 500)&(data['population']>0)]['median_house_value'].mean()

print(avg)