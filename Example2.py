# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
#  описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] => [1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

import random

number = [random.randint(1,30) for i in range(1,random.randint(5,10))]
print(number)
i=1
count = 0
res = []
res.append(number[0])
for i in range(1,len(number)):
    if number[count]< number[i]:
        res.append(number[i])
        count = i
print(res)