# -*- coding: utf8 -*-
# программа, как файловый менеджер, дает выбор действий пользователю (является бесконечной)
import os
print('Здравствуйте! Вас приветсвует программа "Файловый менеджер."')
# Данная функция должна быть глобальной
def go_to_menu():
    print('Операция завершена. Выберите дальнейшие действия.')
    print('[1]. Выход в главное меню.')
    print('[2]. Завершение программы.')
    question = input()
    if question == '1':
        menu()
    elif question == '2':
        print('Спасибо за использование программы.')
        exit()
    else:
        print('Пожалуйста, введите номер ответа корректно.'), go_to_menu()


def menu():
    print('Вы в главном меню. Пожалуйста, выберите номер команды.')
    print('[1]. Запись данных.')
    print('[2]. Вызов файла.')
    print('[3]. Вызов базы данных.')
    print('[4]. Завершение программы.')
    command = input()
    if command == '1':
        username = input('Введите имя пользователя: ')
        user2name = input('Введите фамилию пользователя: ')
        county = input('Страна проживания: ')
        city = input('Город проживания: ')
        age = input('Введите возраст цифрами: ')
        pol = input('Введите пол: ')
        data = {
            'Имя': username,
            'Фамилия': user2name,
            'Страна': county,
            'Город': city,
            'Возраст': age,
            'Пол': pol
        }
        datafile = username + user2name + '.txt'
        def existence_check():
            if os.path.exists(datafile):
                print('Данные для этого пользователя уже сохранены. Вы хотите перезаписать их? ')
                print('[1]. Да')
                print('[2]. Нет')
                question = input()
                if question == '1':
                    with open(datafile, 'w+') as file:
                        file.write(str(data))
                elif question == '2':
                    pass
                else: print('Пожалуйста, введите номер команды корректно.'), existence_check()
            else:
                with open(datafile, 'w+') as file:
                    file.write(str(data))
        existence_check()
        def save_or_not():
            print('Добавить сохраненные данные в базу данных? ')
            print('[1]. Да')
            print('[2]. Нет')
            question = input()
            if question == '1':
                with open('allfiles.txt', 'a') as file:
                    file.write(str(data) + '\n')
            elif question == '2':
                pass
            else:
                print('Пожалуйста, введите номер ответа корректно.'), save_or_not()
        save_or_not()
        go_to_menu()
    elif command == '2':
        filename = input('Пожалуйста, укажите имя файла: ')
        file = open(filename, 'r')
        print(file.read())
        def rewrite_or_not():
            print('Вы хотите перезаписать данные для этого файла?')
            print('[1]. Да')
            print('[2]. Нет')
            rewrite = input()
            if rewrite == '1':
                print('Принято. Введите следующие данные.')
                username = input('Введите имя пользователя: ')
                user2name = input('Введите фамилию пользователя: ')
                county = input('Страна проживания: ')
                city = input('Город проживания: ')
                age = input('Введите возраст цифрами: ')
                pol = input('Введите пол: ')
                data = {
                'Имя': username,
                'Фамилия': user2name,
                'Страна': county,
                'Город': city,
                'Возраст': age,
                'Пол': pol
            }
                file_rewrite = open(filename,'w')
                file_rewrite.write(str(data))
            elif rewrite == '2':
                pass
            else: print('Пожалуйста, введите номер ответа корректно.'), rewrite_or_not()
        rewrite_or_not()
        go_to_menu()
    elif command == '3':
        print('Вы запросили ВСЕ данные о всех пользователях. Загрузка, ожидайте...')
        for i in range(5):
            print('---------------------------')
        print('Данные загружены.')
        allfiles = open('allfiles.txt', 'r')
        print(allfiles.read())
        go_to_menu()
    elif command == '4':
        print('Спасибо за использование программы.')
        exit()




menu()


