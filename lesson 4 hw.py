# Первый вариант:
#     marka_dict = {
#         'Марка': marka,
#     }
#     model_dict = {
#         'Модель': model
#     }
#     year_dict = {
#         'Год выпуска': year
#     }
#     mashina_list = [marka_dict, model_dict, year_dict]
#     print(mashina_list)
# mashina()



# Исправленный вариант:
# mashini_info_list = list()
# mashini_info_dict = dict
# def mashina():
#     marka1 = input('Введите марку первой машины: ')
#     brand1 = input('Введите бренд первой машины: ')
#     model1 = input('Введите модель первой машины: ')
#     year1 = input('Введите год выпуска первой машины: ')
#     marka2 = input('Введите марку второй машины: ')
#     brand2 = input('Введите бренд второй машины: ')
#     model2 = input('Введите модель второй машины: ')
#     year2 = input('Введите год выпуска второй машины: ')
#     marka3 = input('Введите марку третьей машины: ')
#     brand3 = input('Введите бренд третьей машины: ')
#     model3 = input('Введите модель третьей машины: ')
#     year3 = input('Введите год выпуска третьей машины: ')
#     mashini_info_dict= {
#         'Марка первой машины': marka1,
#         'Бренд первой машины': brand1,
#         'Модель первой машины': model1,
#         'Год выпуска первой машины': year1,
#         'Марка второй машины': marka2,
#         'Бренд второй машины': brand2,
#         'Модель второй машины': model2,
#         'Год выпуска второй машины': year2,
#         'Марка третьей машины': marka3,
#         'Бренд третьей машины': brand3,
#         'Модель третьей машины': model3,
#         'Год выпуска третьей машины': year3
#         }
#     mashini_info_list.append(mashini_info_dict)
#     print(mashini_info_list)
# mashina()

#Третий вариант(покороче):
mashina = list()
def mashina_info():
    for info in range(3):
        marka = input('Введите марку машины: ')
        model = input('Введите модель машины: ')
        year = input('Введите год выпуска машины: ')
        mashina_dict = {
            'Марка': marka,
            'Модель': model,
            'Год': year
                }
        mashina.append(mashina_dict)
    print(mashina)
mashina_info()
