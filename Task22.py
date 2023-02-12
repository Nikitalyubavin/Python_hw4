# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

n = int(input('Введите количество элементов первого массива данных: '))
m = int(input('Введите количество элементов второго массива данных: '))

array1 = []
index1 = 0
print('Заполните поэлементно первый массив:')
while (index1 < n):
    array1.append(int(input()))
    index1 += 1

print (f'Первый массив: {array1}')

array2 = []
index2 = 0
print('Заполните поэлементно второй массив:')
while (index2 < m):
    array2.append(int(input()))
    index2 += 1

print (f'Второй массив: {array2}')

def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array[1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

array3 = []
i = 0
while (i < len(array1)):
    if (array1[i] in array2): array3.append(array1[i])
    i += 1

print(f"Повторяющиеся числа: {quick_sort(array3)}")