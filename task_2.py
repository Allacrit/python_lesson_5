"""
Определить индексы элементов массива (списка), значения которых
принадлежат заданному диапазону (т.е. не меньше заданного минимума и не
больше заданного максимума)
"""

from random import randint

new_list = [randint(-10,10) for x in range(20)]
print('Сгенерирован список:\n'
      f'{new_list}')
number_min = int(input('Введите минимальное число: '))
number_max = int(input('Введите максимальное число: '))

print(f'Числа от {number_min} до {number_max} находятся на позициях с номерами:')
for i in range(len(new_list)):
    if number_min <= new_list[i] <= number_max:
        print(i, end=' ')