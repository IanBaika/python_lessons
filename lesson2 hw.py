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