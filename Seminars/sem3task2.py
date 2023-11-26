"""
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
"""
def find_closest_number(arr, target):
    closest_number = float('inf')
    for num in arr:
        diff = abs(num - target)
        if diff < abs(closest_number - target):
            closest_number = num
    return closest_number

# Пример использования

list_1 = [1, 4, 7, 10, 13]

k = 14

closest_number = find_closest_number(list_1, k)

print(closest_number)
