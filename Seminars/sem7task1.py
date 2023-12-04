"""
Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента
 функцию, вычисляющую элемент по номеру строки и столбца.

Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.

Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).

Если строк меньше двух, выдайте текст
ОШИБКА! Размерности таблицы должны быть больше 2!.

Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента,
как, например, у операции умножения.

"""


# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 3 or num_columns < 3:
#         print('ОШИБКА! Размерности таблицы должны быть больше 2!')
#     else:
#         for row in range(1, num_rows + 1):
#             for column in range(1, num_columns + 1):
#                 print(operation(row, column), end='\t')
#             print()
#
# print_operation_table(lambda x, y: x + y, 4, 4)

def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 or num_columns < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        header = ' '.join([str(i) for i in range(1, num_columns + 1)])
        print(header)
        for i in range(2, num_rows + 1):
            row = [str(i)] + [str(operation(i, j)) for j in range(2, num_columns + 1)]
            print(' '.join(row))

print_operation_table(lambda x, y: x * y, 10, 10)