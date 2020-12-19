day = int(input('Введите числом ваш день рождения:'))
month = int(input('Введите числом ваш месяц рождения:'))
year = int(input('Введите свой год рождения:'))
if (day > 21 and day < 31 and month == 3) or (day > 1 and day < 20 and month == 4):
    print ("Ваш знак зодиака: Овен")
elif (day > 21 and day < 31 and month == 4) or (day > 1 and day < 20 and month == 5):
    print ("Ваш знак зодиака: Телец")
elif (day > 21 and day < 31 and month == 5) or (day > 1 and day < 20 and month == 6):
    print ("Ваш знак зодиака: Близнецы")
elif (day > 21 and day < 31 and month == 6) or (day > 1 and day < 20 and month == 7):
    print ("Ваш знак зодиака: Рак")
elif (day > 21 and day < 31 and month == 7) or (day > 1 and day < 20 and month == 8):
    print ("Ваш знак зодиака: Лев")
elif (day > 21 and day < 31 and month == 8) or (day > 1 and day < 20 and month == 9):
    print ("Ваш знак зодиака: Дева")
elif (day > 21 and day < 31 and month == 9) or (day > 1 and day < 20 and month == 10):
    print ("Ваш знак зодиака: Весы")
elif (day > 21 and day < 31 and month == 10) or (day > 1 and day < 20 and month == 11):
    print ("Ваш знак зодиака: Скорпион")
elif (day > 21 and day < 31 and month == 11) or (day > 1 and day < 20 and month == 12):
    print ("Ваш знак зодиака: Стрелец")
elif (day > 21 and day < 31 and month == 12) or (day > 1 and day < 20 and month == 1):
    print ("Ваш знак зодиака: Козерог")
elif (day > 21 and day < 31 and month == 1) or (day > 1 and day < 20 and month == 2):
    print ("Ваш знак зодиака: Водолей")
elif (day > 21 and day < 31 and month == 2) or (day > 1 and day < 20 and month == 3):
    print("Ваш знак зодиака: Рыбы")
x_int = 2020
print('Ваш возраст:',  x_int - int(year))