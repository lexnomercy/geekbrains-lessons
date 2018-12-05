#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math
import re

__author__ = "Орехов Алексей Александрович"


# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1

def randomDigit():
    a = random.uniform(0, 9)
    return (a)

n = int(randomDigit())
m = int(randomDigit())

print(n, m)


def fibonacci(n, m):
    fib = []
    a, b = 0, 1
    for num in range(m):
        fib.append(b)
        a, b = b, a+b
    n -= 1
    res = [fib[i] for i in range(n, m)]
    del fib
    print(res)
    return res


# Функция для проверки порядка последовтаельности, для нас важно, чтобы m был больше n.
def compareElem(n, m):
    while True:
        if m < n:
            m = int(randomDigit())
            n = int(randomDigit())
            continue
        else:
            fibonacci(n, m)
            break
    return fibonacci(n,m)

compareElem(n, m)


# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


#Генерим список
numberList = [random.randint(-99, 99) for i in range(10)]
#print(numberList)

def sort_list(list):
    # print (numberList)
    sorted_list = [] # Создаем пустой список
    while len(numberList) > 0: # Пока количество элементов изначального списка не равно 0
        a = numberList[0] # переменная а принимает значение первого элемента изначального списка
        for i in numberList: # цикл проверки
            if i <= a: # если перемнная прохода выпоняет условие
                a = i # перемнная принимает значение перемнной прохода
        numberList.remove(a) # убираем элемент из первоначального списка, тем самы сокращая количестово элелемнтов
        sorted_list.append(a) # к новому списку в конец аттачим полученное значение
    print (sorted_list) #

sort_list(numberList) #


# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.

numberList = [random.randint(7, 9) for i in range(10)]
#print(numberList)

def filter_func(arg, list):
    filtered_list = []
    for i in list:
        if i != arg: # тцут все просто, если элемент не равен аргументу, добавляем его в новый список
            filtered_list.append(i)
    print(numberList)
    print (filtered_list)

filter_func(9, numberList)



# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


A1, A2, A3, A4 = (1, 1), (3, 2), (3, 6), (1, 5)


def parallelogram(a, b, c, d):
    # ищем признаки парраллелограмма
    side1 = False
    side2 = False

    ab = math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)
    cb = math.sqrt((b[0] - c[0])**2 + (b[1] - c[1])**2)
    cd = math.sqrt((d[0] - c[0])**2 + (d[1] - c[1])**2)
    ad = math.sqrt((d[0] - a[0])**2 + (d[1] - a[1])**2)
    if ab == cd and cb == ad:
        print("Стороны AB({}) - CD({}) и CB({}) - AD({}), равны".format(round(ab), round(cd), cb, ad))
        side1 = True
    else:
        print('Противоположные стороны НЕ равны')
    #Проверка: диагонали параллелограмма точкой пересечения делятся пополам
    diagonal1 = ((a[0] + c[0])/2, (a[1] + c[1])/2)
    diagonal2 = ((b[0] + d[0])/2, (b[1] + d[1])/2)
    if diagonal1 == diagonal2:
        side2 = True
    if side1 and side2:
        print('Вершины A1%s, A2%s, A3%s, A4%s образуют параллелограмм' % (a, b, c, d))
    else:
        print('Проверьте точки вершин')

parallelogram(A1, A2, A3, A4)
