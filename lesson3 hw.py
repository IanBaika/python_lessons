# Задание 1. Первый способ:
i = 700
while i // 7:
    print(i)
    i -= 7
#Второй способ (с range):
i = 0
while i in range(0,700,7):
    print(i)
    i += 7
# Задание 2.
name = input('Введите имена людей одинакового пола: ')
pol = input('Введите пол: (мужской/женский): ')
men = list()
women = list()
if pol == 'мужской':
    men.append(name)
elif pol == 'женский':
    women.append(name)
if len(men) == 0:
    print('Вы не ввели данных для мужчин')
    name = input('Введите имена мужчин: ')
    men.append(name)
if len(women) == 0:
    print('Вы не ввели данных для девушек')
    name = input('Введите имена девушек: ')
    women.append(name)
if len(men) > 5:
    print('Вы ввели недопустимое количество данных для мужчин')
elif len(women) > 5:
    print('Вы ввели недопустимое количество данных для девушек')
elif len(men) or len(women) <= 5:
    print('Список мужчин:',men,'\nСписок девушек:',women)
