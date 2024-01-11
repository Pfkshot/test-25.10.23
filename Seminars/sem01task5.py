"""
Задача №5. Решение в группах
Вагоны в электричке пронумерованы натуральными
числами, начиная с 1 (при этом иногда вагоны
нумеруются от «головы» поезда, а иногда – с
«хвоста»; это зависит от того, в какую сторону едет
электричка). В каждом вагоне написан его номер.
Витя сел в i-й вагон от головы поезда и обнаружил,
что его вагон имеет номер j. Он хочет определить,
сколько всего вагонов в электричке. Напишите
программу, которая будет это делать или сообщать,
что без дополнительной информации это сделать
невозможно.
Input: 3 4(ввод на разных строках)
Output: 6
"""

"""
Задачка решается тогда, когда Витя не угадал с началом нумерации вагонов. 
То-есть, например, Витя прибежал на вокзал, а поезд уже отправлялся -
и он запрыгнул во второй вагон, с хвоста поезда. Затем он узнал у контролера, 
что на самом деле - это 8-ой вагон и нумерация начинается с головы поезда. 
Поэтому путём вычисления 8+2-1 получаем, что вагонов всего 9. 
Но если бы, контролер сказал Вите, что это 2-ой вагон, и
нумерация вагонов идёт с хвоста - то Вите это ничего бы не дало, 
и кроме как пройтись и посчитать количество вагонов до головы 
поезда - ему больше ничего не остаётся.

Нужно отсечь сам вагон, в котором мы сидим
"""

i = 2
j = 3
if i == j:
    print("Задачу без доп. условий решить невозможно")
else:
    print(f"Количество вагонов: {i + j - 1}")