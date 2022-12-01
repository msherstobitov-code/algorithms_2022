"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Попробуйте оптимизировать код, чтобы снизить время выполнения
Проведите повторные замеры

ОБЯЗАТЕЛЬНО! Добавьте аналитику: что вы сделали и какой это принесло эффект
"""
from timeit import timeit

def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr

# списковое включение

def func_2(nums):
    return [x for x in nums if x % 2 == 0]

# 1000
NUMS = [el for el in range(1000)]
print(
    timeit("func_1(NUMS[:])"),
    globals = globals(),
    number = 1000)
print(
    timeit("func_2(NUMS[:])"),
    globals = globals(),
    number = 1000)

#10000
NUMS =[el for el in range(10000)]
print("-------------------------------------------------------")
print(
    timeit("func_1(NUMS[:])"),
    globals = globals(),
    number = 1000)
print(
    timeit("func_2(NUMS[:])"),
    globals = globals(),
    number = 1000)