print("Задание", 1)
import datetime

now = datetime.datetime.now()

formatted_date_1 = now.strftime('%d.%m.%Y')
print(formatted_date_1)

formatted_date_2 = now.strftime('%d.%m.%y')
print(formatted_date_2)

formatted_date_3 = now.strftime('%d %b %Y')
print(formatted_date_3)

formatted_date_4 = now.strftime('%d %B %y')
print(formatted_date_4)

formatted_date_5 = now.strftime('%d.%m.%Y - день в году: %j неделя: %U день недели: %A')
print(formatted_date_5)

formatted_date_6 = now.strftime('Точное время: %I:%M:%S')
print(formatted_date_6)

formatted_date_7 = now.strftime('Точное время: (%p): %I:%M:%S')
print(formatted_date_7)

print("Задание", 2)
import time

my_local_time = time.localtime()
my_time = time.strftime('Сегодня: %A %d %B %Y %I:%M:%S %d.%m.%Y', my_local_time)
print(my_time)

print("Задание", 3)

import time

for i in range(0,5):
    print(i)
    time.sleep(3)