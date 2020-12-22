#Списком времена года:
month = int(input('Введите нынешний месяц числом: '))
winter = [1,2,12] #список
spring = [3,4,5]
summer = [6,7,8]
autumn = [9,10,11]
if month in winter: #если число месяца входит в индекс зимы, то
    print('Сейчас зима')
elif month in spring:
    print('Сейчас весна')
elif month in summer:
    print('Сейчас лето')
elif month in autumn:
    print('Сейчас осень')


#Проверка на количество символов:
phrase = input('Введите фразу или слово: ')
if len(phrase) > 10:
    print('Нельзя вводить так много символов')
else: print('Вы ввели допустимое количество символов')
    
# Практическое задание с 48й строки: 
number = 16
second_number = not 1
first_array = [1, 2, 3]
second_array = [1, 2]

if number > 15:
    print("1")

if first_array:
    print("2")

if len(second_array) == 2:
    print("3")

if len(first_array) + len(second_array) == 5:
    print("4")

if first_array and first_array[0] == 1:
    print("5")

if not second_number:
    print("6")
