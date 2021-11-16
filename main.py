class cordinate_not_in_range(Exception):
    pass
class Illegl_move(Exception):
    pass
side_border = '|'
border_symbol = '-'
import time
import shutil
def print_centre(s):
    print(s.center(shutil.get_terminal_size().columns))
def create_tic_tac_toe_board(n):
    # will return an a list of list containing all the elements in the borad
    tic_tac_toe = []
    for i in range(n):
        tic_tac_toe.append([])
        for j in range(n):
            tic_tac_toe[i].append('-')
    return tic_tac_toe
def display_default():
    print_centre('WELCOME TO THE GAME OF TIC TAC TOE')
    print_centre('PLAYER 1 IS X')
    print_centre('PLAYER 2 IS O')
    print_centre('ENTER THE COORDINATES IN THE FORMAT X Y')
    print_centre('WHERE X IS THE X COORDINATE AND Y IS THE Y COORDINATE ')
    print_centre('0 0 is the top left corner')

def display(tic_tac_toe):
    for i in tic_tac_toe:
        print(*i,sep='    ')
def fancy_display(tic_tac_toe):
    lines = []
    s = ''
    for i in range(2*len(tic_tac_toe)+ 1):
        s = s + border_symbol+' '
    lines.append(s)
    for i in tic_tac_toe:
        t = side_border + ' '
        t = t + ' {} '.format(side_border).join(i) + ' {}'.format(side_border)
        lines.append(t)
        lines.append(s)
    for i in lines:
        print_centre(i)
def game():
    display_default()
    size_of_the_borad = 3
    tic_tac_toe = create_tic_tac_toe_board(size_of_the_borad)
    turn = 1
    state = -1
    while(state == -1):
        fancy_display(tic_tac_toe)
        print_centre("PLAYER {}'S TURN".format(turn))
        print_centre('ENTER THE COORDINATES')
        cord = input().split()
        x_cord = int(cord[0])
        y_cord = int(cord[1])
        try:
            if x_cord >= size_of_the_borad or  y_cord >= size_of_the_borad:
                raise cordinate_not_in_range
            elif tic_tac_toe[x_cord][y_cord] != '-':
                raise Illegl_move
        except cordinate_not_in_range:
            print_centre('THE ENTERED NUMBER IS NOT IN THE RANGE')
            print_centre('PLEASE TRY AGAIN')
            continue
        except Illegl_move:
            print_centre('ALDREADY FILLED')
            print_centre('PLEASE TRY AGAIN')
            continue
        if turn == 1:
            tic_tac_toe[x_cord][y_cord] = 'X'
            turn = 2
        else:
            tic_tac_toe[x_cord][y_cord] = 'O'
            turn = 1

def main():
    game()
if __name__ == '__main__':
    main()
