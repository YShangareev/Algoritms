# Быстрая сортировка

import random
# Создаем функцию для сравнения всех элементов массива
def quick_sort(my_list):
    # Если длина массива меньше двух
    if len(my_list) < 2:
        # Выводим этот массив
        # Базовый случай
        return my_list
    else:
        # Иначе назначаем случайную опорную точку
        pivot = random.choice(my_list)
        # Аргументы меньше опорного элемента
        lowest = [i for i in my_list[0:] if i < pivot]
        # Аргументы больше опорного элемента
        greater = [i for i in my_list[0:] if i > pivot]
        # Возвращаем список меньше + опорную точку + больше
        return quick_sort(lowest) + [pivot] + quick_sort(greater)

my_list = [1, 25, 68, 10, 30, 2]
print(quick_sort(my_list))