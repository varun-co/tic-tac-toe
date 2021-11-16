def create_tic_tac_toe_board(n):
    # will return an a list of list containing all the elements in the borad
    tic_tac_toe = []
    for i in range(n):
        tic_tac_toe.append([])
        for j in range(n):
            tic_tac_toe[i].append('#')
    return tic_tac_toe
def display(tic_tac_toe):
    for i in tic_tac_toe:
        print(*i,sep='    ')
#def fancy_display()

def main():
    tic_tac_toe = create_tic_tac_toe_board(3)
    display(tic_tac_toe)
if __name__ == '__main__':
    main()
