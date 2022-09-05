# Сортировка выбором

my_list = [45, 66, 1, 78, 2, 14, 16, 99]
print('Было', my_list)

for i in range(len(my_list)):
    # Первый элемент примем за наименьший
    smallest = i
    # Далее задаем условие для второго элемента последовательности
    for a in range(i+1, len(my_list)):
        # Если второй элемент оказывается меньше первого, то он заменяет его и становится первым
        if my_list[a] < my_list[smallest]:
            smallest = a
    # Далее мы задаем условие, которое меняет местами наши значения
    my_list[i], my_list[smallest] = my_list[smallest], my_list[i]

print('Стало', my_list)
