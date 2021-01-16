# -*- coding: utf8 -*-
class Worker:  # создаю класс Worker
    def __init__(self,salary = 3000): # задаю зарплату по умолчанию
        self.salary = salary

    def __del__(self):  # создаю деструктор
        print('Рабочий уволен')


    def work(self):  # задаю ему метод work
        print('Рабочий делает ручную работу. Зарплата -', self.salary, 'сом.')  # Возвращаю информацию


class Driver(Worker):  # создаю наследующий от класса Workek класс Driver
    __has_car = True  # задаю ему неизменяемое свойство

    def __init__(self, salary=5000):  # задаю зарплату по умолчанию
        self.salary = salary

    def work(self):  # Возвращаю информацию
        print('Водитель водит машину. Зарплата -', self.salary, 'сом.', self.__has_car)

    def __del__(self):  # создаю деструктор
        print('Водитель уволен')

# Создаю объекты класса Driver, вызываю им метод work
Adam = Driver(10000) 
Adam.work()

# Создаю объекты класса Worker, вызываю им метод work
Ravshan = Worker()
Ravshan.work()
