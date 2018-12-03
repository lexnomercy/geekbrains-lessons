
# Задача-1:
# Дан список, заполненный произвольными целыми числами, получите новый список,
# элементами которого будут квадратные корни элементов исходного списка,
# но только если результаты извлечения корня не имеют десятичной части и
# если такой корень вообще можно извлечь
# Пример: Дано: [2, -5, 8, 9, -25, 25, 4]   Результат: [3, 5, 2]


import random
import math
randomList = [random.randint(0, 5) for i in range(10)]
sqrtList = []
for i in randomList:
    if i > 0:
        x = math.sqrt(i)
        if i % x == 0:
            sqrtList.append(x)

print(randomList)
print(sqrtList)



# Задача-2: Дана дата в формате dd.mm.yyyy, например: 02.11.2013.
# Ваша задача вывести дату в текстовом виде, например: второе ноября 2013 года.
# Склонением пренебречь (2000 года, 2010 года)

from datetime import datetime, date, time


dt = datetime.now()

varDay = (f"{dt:%d}")
varMonth = (f"{dt:%m}")
varYear = (f"{dt:%Y}")
varHour = (f"{dt:%H}")
varMinute = (f"{dt:%M}")
varSecond = (f"{dt:%S}")

#print(str(varDay))

event_date = str(varDay + "." + varMonth + "." + varYear)

#print(event_date)

days = [
    'первое', 'второе', 'третье', 'четвертое', 'пятое', 'шестое', 'седьмое', 'восьмое',
    'девятое', 'десятое', 'одиннадцатое', 'двенадцатое', 'тринадцатое', 'четырнадцатое',
    'пятнадцатое', 'шестнадцатое', 'семнадцатое', 'восемнадцатое', 'девятнадцотое', 'двадцатое',
    'двадцать первое', 'двадцать второе', 'двадцать третье', 'двадцать четвертое', 'двадцать пятое',
    'двадцать шестое', 'двадцать седьмое', 'двадцать восьмое', 'двадцать девятое', 'тридцатое',
    'тридцать первое'
]
months = [
    'января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа',
    'сентября', 'октября', 'ноября', 'декабря'
]

date_list = event_date.split('.')

#print(date_list)

day = days[int(date_list[0])-1]
month = months[int(date_list[1])-1]
year = int(date_list[2])

print('Сегодня: %s %s %s года' % (day, month, year))
for i in varHour:
    if int(i) <= 1:
        print("Текущее время: " + varHour + " час" + varMinute + " минут")
    elif int(i) > 1 and int(i) <= 3:
        print("Текущее время: " + varHour + " часа" + varMinute + " минут")
    elif int(i) > 3 and int(i) < 21:
        print("Текущее время: " + varHour + " час" + varMinute + " минут")


# Задача-3: Напишите алгоритм, заполняющий список произвольными целыми числами
# в диапазоне от -100 до 100. В списке должно быть n - элементов.
# Подсказка:
# для получения случайного числа используйте функцию randint() модуля random
import random
n = input('Введите любое число: ')
n = int(n)
listForNKey = [random.randint(-100, 100) for i in range(n)]
print(listForNKey)



# Задача-4: Дан список, заполненный произвольными целыми числами.
# Получите новый список, элементами которого будут:
# а) неповторяющиеся элементы исходного списка:
# например, lst = [1, 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 2, 4, 5, 6]
# б) элементы исходного списка, которые не имеют повторений:
# например, lst = [1 , 2, 4, 5, 6, 2, 5, 2], нужно получить lst2 = [1, 4, 6]

listForСompare = [random.randint(0, 10) for i in range(10)]
ComparedList = set(listForСompare)
ComparedList = list(ComparedList)
print(listForСompare)
print(ComparedList)

AnotherList = [x for x in listForСompare if not listForСompare.count(x) > 1]
print(AnotherList)
