# Задача 3. Задайте список случайных чисел от 1 до 10.
#  Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают 
# Список уникальных элементов [1, 4, 2, 3, 6, 7]

import random

number = [random.randint(1,10) for i in range(1,random.randint(5,15))]
print(number)

print([i for n,i in enumerate(number) if i not in number[:n]])


