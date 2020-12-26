marka_dict = dict
model_dict = dict
year_dict = dict
mashina_list = list()
def mashina():
    marka = input('Марка:')
    model = input('Модель:')
    year = input('Год выпуска:')
    marka_dict = {
        'Марка': marka,
    }
    model_dict = {
        'Модель': model
    }
    year_dict = {
        'Год выпуска': year
    }
    mashina_list = [marka_dict, model_dict, year_dict]
    print(mashina_list)
mashina()