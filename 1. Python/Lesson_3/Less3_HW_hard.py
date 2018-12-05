#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math

__author__ = "Орехов Алексей Александрович"


# Задание-1:
# Написать программу, выполняющую операции (сложение и вычитание) с простыми дробями.
# Дроби вводятся и выводятся в формате:
# n x/y ,где n - целая часть, x - числитель, у - знаменатель.
# Дроби могут быть отрицательные и не иметь целой части, или иметь только целую часть.
# Примеры:
# Ввод: 5/6 + 4/7 (всё выражение вводится целиком в виде строки)
# Вывод: 1 17/42  (результат обязательно упростить и выделить целую часть)
# Ввод: -2/3 - -2
# Вывод: 1 1/3





# Задание-2:
# Дана ведомость расчета заработной платы (файл "data/workers").
# Рассчитайте зарплату всех работников, зная что они получат полный оклад,
# если отработают норму часов. Если же они отработали меньше нормы,
# то их ЗП уменьшается пропорционально, а за заждый час переработки
# они получают удвоенную ЗП, пропорциональную норме.
# Кол-во часов, которые были отработаны, указаны в файле "data/hours_of"

workers = open("C:/Geekbrains/workers.txt", "r") #
salary = open("C:/Geekbrains/salary.txt", "r") #
hourly_list = open("C:/Geekbrains/hourly_list.txt", "r") #

surnames = workers.read().split('\n') # Создаем список фамилий
wage_rate = salary.read().split('\n') # базовая ставка ЗП
hourly_calculation = hourly_list.read().split('\n') # фактическое количество отработанных часов

base_weekly_rate = 40 # Базовое количество часов в неделю.
a = len(surnames)

def salary_calculate():
    # Проверяем ведомости на количество элементов.
    # for i in range(1):
    if len(surnames) == len(wage_rate) == len(hourly_calculation):
        print("Ведомости в порядке")
    else:
        print("Проверьте ведомости!! \nНе хватает данных!!")
        return

    for i in range(a):
        h = int(hourly_calculation[i])
        print("Работник: {}. Базовая ставка {}. Отработал: ".format(surnames[i], wage_rate[i]), h, " часов")
        if h == base_weekly_rate:
            print("Заработная плата составила : {}".format(wage_rate[i]))
        elif h < base_weekly_rate:
            x = int(hourly_calculation[i]) * (int(wage_rate[i]) / base_weekly_rate)
            print("Заработная плата составила : {}".format(x))
        elif h > base_weekly_rate:
            z = int(wage_rate[i]) + ((int(hourly_calculation[i]) - base_weekly_rate) * (int(wage_rate[i]) / base_weekly_rate))
            print("Заработная плата составила : {}".format(z))
            continue

salary_calculate()

# Задание-3:
# Дан файл ("data/fruits") со списком фруктов.
# Записать в новые файлы все фрукты, начинающиеся с определенной буквы.
# Т.е. в одном файле будут все фрукты на букву “А”, во втором на “Б” и т.д.
# Файлы назвать соответственно.
# Пример имен файлов: fruits_А, fruits_Б, fruits_В ….
# Важно! Обратите внимание, что нет фруктов, начинающихся с некоторых букв.
# Напишите универсальный код, который будет работать с любым списком фруктов
# и распределять по файлам в зависимости от первых букв, имеющихся в списке фруктов.
# Подсказка:
# Чтобы получить список больших букв русского алфавита:
# print(list(map(chr, range(ord('а'), ord('я')+1))))
