"""
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.

Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его.

Будем считать, что на вход подается только одно слово, которое содержит либо только английские,
либо только русские буквы.
"""

import re
#Определяем язык
def isCyrillic(text):
	return bool(re.search('[а-яА-Я]', text))
#Задаем очки за буквы через словарь
points_en = {1:'AEIOULNSTR',
      	2:'DG',
      	3:'BCMP',
      	4:'FHVWY',
      	5:'K',
      	8:'JZ',
      	10:'QZ'}
points_ru = {1:'АВЕИНОРСТ',
      	2:'ДКЛМПУ',
      	3:'БГЁЬЯ',
      	4:'ЙЫ',
      	5:'ЖЗХЦЧ',
      	8:'ШЭЮ',
      	10:'ФЩЪ'}
#Вводим слово
print('Введите слово на русском или английском языке')
text = input().upper()
#Выводим сумму
if isCyrillic(text):
	print(sum([k for i in text for k, v in points_ru.items() if i in v]))
else:
	print(sum([k for i in text for k, v in points_en.items() if i in v]))
# k = 'ноутбук'
#
# eng = 'qwertyuiopasdfghjklzxcvbnm'
#
# rus = 'йцукенгшщзхъфывапролджэячсмитьбюё'
#
# list_English = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP',
#                 4:'FHVWY', 5:"K" , 8:'JX', 10:'QZ'}
# list_Russian = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ',
#                 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
# word = k
# if word[0].lower() in eng:
#     summa = 0
#     for letter in word:
#         for key, value in list_English.items():
#             if letter.upper() in value:
#                 summa += key
#     print(summa)
# else:
#     if word[0].lower() in rus:
#         summa = 0
#         for letter in word:
#
#             for key, value in list_Russian.items():
#                 if letter.upper() in value:
#                     summa += key
#     print(summa)
