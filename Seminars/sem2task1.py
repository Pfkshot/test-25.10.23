"""
На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом.
Ваша задача - определить минимальное количество монеток, которые нужно перевернуть,
 чтобы все монетки лежали одной и той же стороной вверх.

Входные данные:

На вход программе подается список coins, где coins[i] равно 0, если i-я монетка лежит гербом вверх,
и равно 1, если i-я монетка лежит решкой вверх.
Размер списка не превышает 1000 элементов.
"""

coins = [0, 1, 0, 1, 1, 1, 1]
n = len(coins)
a = 0
b = 0
for i in range(n):
    if coins[i] == 1:
        a += 1
    else:
        b += 1
print()
if a > b:
    print(f'Нужно перевернуть {b} монеток')
else:
    print(f'Нужно перевернуть {a} монеток')
