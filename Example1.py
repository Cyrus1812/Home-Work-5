# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5. 
# Используйте для решения лямбда-функцию.
# 2, 3, 4, 6, 7, 8 -> 6, 7, 8

import random
number = [random.randint(1,11) for i in range(10)]
print(number)
print(list(filter(lambda x: (x>5),number)))