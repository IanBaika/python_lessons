# -*- coding: utf8 -*-
class Worker: #создаю класс Worker
    salary = 3000 # ставлю зарплату по умолчанию 3000
    def work(self): #задаю ему метод work
        print('Рабочий делает ручную работу. Зарплата -', self.salary, 'сом.') # Возвращаю информацию
class Driver(Worker): #создаю наследующи от класса Workek класс Driver
    has_car = True #задаю ему неизменяемое свойство
    def __init__(self,salary): #зарплата задается пользователем
        self.salary = salary
    def work(self): #Возвращаю информацию
        print('Водитель водит машину. Зарплата -', self.salary, 'сом.', self.has_car)
    def __del__(self): #создаю деструктор
        print('Водитель уволен')
# Создаю объекты класса, вызываю им метод work
Adam = Driver(10000)
Adam.work()
Ravshan = Worker()
Ravshan.work()
