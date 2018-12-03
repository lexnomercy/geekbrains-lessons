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
