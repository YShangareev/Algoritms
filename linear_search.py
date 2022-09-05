# Линейный(тупой) поиск
# Проходит по всем элементам списка O(n)
my_list = [25, 55, 87, 69, 45, 10, 11]

def linear_search(where, what):
    for i in enumerate(where):
        if i[1] == what: # Если первый элемент = искомому элементу
            return i[0]  # то выводим индекс 0
    return None          # если ничего не найдено, то None


print(linear_search(my_list, 10))
