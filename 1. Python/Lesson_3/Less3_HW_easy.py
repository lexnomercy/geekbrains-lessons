#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random
import math
import re

__author__ = "Орехов Алексей Александрович"

# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом)
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math

# Генерим псевдослучайное число в диапазоне от 0 до 9. Почему не от 0? Чтобы во втором вызове получить честное округление
def randomDigit():
    a = random.uniform(0, 9)
    return (a)

#Присваиваем переменной и говорим что число с плавающей запятой - его мы будем использовать для округления
a = float(randomDigit())

# Еще раз запускаем генератор и поредаем число, на котрое будем в итоге округлять
b = int(randomDigit())

def round(a, b):
    powDgt = pow(10,b)
    combined =  a * powDgt
    intComb = int(combined)
    rounded = combined - intComb
    if not (abs(rounded) < 0.5):
        if intComb > 0: intComb += 1
        else: intComb -= 1
    return intComb/powDgt

if b != 0:
    g = round(a, b)
else:
    g = int(round(a, b))

# Принты выводятся только для проверки чистоты выполнения
print(a)
print (b)
print(g)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


# ticketNumber = list(random.sample(range(000000, 999999), 1))

ticketNumber = [random.randint(0, 9) for i in range(6)]
# ticketNumber = [1, 2, 3, 1, 2, 3]
# a = int(len(ticketNumber))
# print(a)

# print(ticketNumber)


# Слишком громоздкое решение
def LuckyTicket(ticketNumber):
    if ticketNumber[0] + ticketNumber[1] + ticketNumber[2]== ticketNumber[3] + ticketNumber[4] + ticketNumber[5]:
        print("Wow")
    else: print("Too bad")

# Более короткое решение
def LuckyTicketSum(ticketNumber):
    if sum(ticketNumber[:3]) == sum(ticketNumber[3:]):
        print("Perfecto seniore")
    else: print("Terribile, compra un nuovo biglietto, seniore")

print(ticketNumber)
a = LuckyTicket(ticketNumber)
print(ticketNumber)
b = LuckyTicketSum(ticketNumber)
