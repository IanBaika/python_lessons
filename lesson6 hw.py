pole = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
def draw_board():
    for i in range(3):
        print('\n', pole[i])
        i += 1
draw_board()
def game():
    def take_input(value):
        player_answer = input('Куда поставим ' + value + '? ')
        try:
            player_answer = int(player_answer)
        except ValueError:
            print("Некорректный ввод. Вы уверены, что ввели число?"), game()
        if int(player_answer) >= 1 and int(player_answer) <=3:
            x = 0
            y = int(player_answer) - 1
            pole[x][y] = value
        elif int(player_answer) >= 4 and int(player_answer) <= 6:
            x = 1
            y = int(player_answer) - 4
            pole[x][y] = value
        elif int(player_answer) >= 7 and int(player_answer) <= 9:
            x = 2
            y = int(player_answer) - 7
            pole[x][y] = value
        else: print("Некорректный ввод. Введите число от 1 до 9."), game()
    counter = 0
    while counter != 9:
        if counter % 2 == 0:
            take_input('X')
            draw_board()
        else: take_input('О'), draw_board()
        counter += 1
game()