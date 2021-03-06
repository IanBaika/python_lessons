import os
# Я немного разнообразил д/з, добавив некоторые данные и интерактив с пользователем
# Запрос основной информации
username = input('Введите имя пользователя: ')
user2name = input('Введите фамилию пользователя: ')
# Запрос дополнительной информации
print('Введите необходимые данные')
# 4 доп. пункта о пользователе.
county = input('Страна проживания: ')
city = input('Город проживания: ')
age = int(input('Введите возраст цифрами: '))
pol = input('Введите пол: ')
# Избежание различных ошибок в заполнении данных, требующих буквенное значение.
while county == int or county == float:
    print('Вы ввели данные для запроса о стране проживания неверно. Попробуйте еще раз!')
    county = input('Страна проживания: ')
while city == int or city == float:
    print('Вы ввели данные для запроса о городе проживания неверно. Попробуйте еще раз!')
    city = input('Город проживания: ')

# Сохранение данных в словарь
data = {
    'Имя': username,
    'Фамилия': user2name,
    'Страна': county,
    'Город': city,
    'Возраст': age,
    'Пол': pol
}
# Если пользователь ввел данные, которые уже есть, будет уточнение, перезаписать файла или нет
datafile = username + user2name    # для названия файла
question = ''
if os.path.exists(datafile + '.txt'):
     question = input('Данные для этого пользователя уже сохранены. Вы хотите перезаписать их? (Да/Нет) ')
     if question == 'Да':
         with open(datafile + '.txt', 'w+') as file:
             file.write(str(data))
     elif question == 'Нет':
         pass
else:
    with open(datafile + '.txt','w+') as file:
        file.write(str(data))

# Добавление данных в "базу данных" (файл со всеми данными)
with open('allfiles.txt','a') as file:
    file.write(str(data) + '\n')

# Чтение определенного файла
question1 = input('Вы хотите прочесть данные определенного файла? (Да/Нет) ')
question2 = ''
if question1 == 'Да':
    question2 = input('Укажите файл: ')
    filename = open(question2, 'r')
    print(filename.read())
if question1 == 'Нет':
    pass

# Чтение "базы данных" (файла со всеми данными)
allfiles = open('allfiles.txt', 'r')
question3 = input('Хотите запросить все данные о всех пользователях? (Да/Нет) ')
if question3 == 'Да':
    print(allfiles.read())
if question3 == 'Нет':
    pass


# 1. Написать программу, которая запрашивает и сохраняет данные о пользователе в файл
# Запрос и сохранение данных ✔
# 2. Для каждого пользователя заводится отдельный файл, предварительно проверив, есть ли уже с таким именем
# Проверка на наличие файла и создание файлов  ✔
# 3. У программы три режима работы - вывод всех файлов с пользователями;
# Файл с данными всех пользователей  ✔
# 3.1 Выбор файла и вывод данных;
# Выбор файла и чтение выбранного файла  ✔
# 3.2 Создание новой записи, путем введения новых данных;
#   ✔
