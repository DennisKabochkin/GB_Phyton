#2. Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().
list_1 = input("Введите числа через _").split('_')
a, b = 0, 1
while len(list_1) > b:
    list_1[a], list_1[b] = list_1[b], list_1[a]
    a +=2
    b+=2
print('Результат', *list_1)