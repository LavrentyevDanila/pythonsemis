# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

list = [2, 3, 6, 8, 1, 7]

if len(list)%2 == 0:
    size = len(list) // 2
import math 
size = math.ceil(len(list)/2)
print(size)
list2 = []
for i in range(size):
    list2.append(list[i]*list[-i - 1])
print(list2)