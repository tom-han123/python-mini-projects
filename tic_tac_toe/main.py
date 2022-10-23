
def insert_letter(letter, pos):
    board[pos] = letter

def is_SpaceFree(pos):
    return board[pos] == ' '

def printboard(board):
    print('   |   |   ')
    print(' '+board[1]+' | '+board[2]+' | '+board[3]+' ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' ')
    print('   |   |   ')
    print('------------')
    print('   |   |   ')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' ')
    print('   |   |   ')

def isWinner(board, letter):
    return (board[1] == letter and board[2] == letter and board[3] == letter or
            board[4] == letter and board[5] == letter and board[6] == letter or
            board[7] == letter and board[8] == letter and board[9] == letter or
            board[1] == letter and board[4] == letter and board[7] == letter or
            board[2] == letter and board[5] == letter and board[8] == letter or
            board[3] == letter and board[6] == letter and board[9] == letter or
            board[1] == letter and board[5] == letter and board[9] == letter or
            board[3] == letter and board[5] == letter and board[7] == letter)

def playermove():
    run = True
    while run:
        move = input('Input the position you want to move (1-9)')
        try:
            move = int(move)
            if move > 0 or move < 10:
                if is_SpaceFree(move):
                    run = False
                    insert_letter('X', move)
                else:
                    print(' The position is occupied ')
            else:
                print(' Index out of range ')
        except:
            print('Please enter a digit number')

def compmove():
    possible_pos = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0

    for l in ('X', 'O'):
        for i in possible_pos:
            board_copy = board[:]
            board_copy[i] = l
            if isWinner(board_copy, l):
                move = i
                return move

    corners = []
    for i in possible_pos:
        if i in [1, 3, 7, 9]:
            corners.append(i)

    if len(corners) > 0:
        move = randon_select(corners)
        return move

    edges = []
    for i in possible_pos:
        if i in [2, 4, 6, 8]:
            edges.append(i)

    if len(edges) > 0:
        move = randon_select(edges)
        return move

    return move

def randon_select(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]

def is_board_full(board):
    if board.count(' ') > 1:
        return False
    else:
        return True


def main():
    print(' Welcome to Tic Tac Toe ')
    printboard(board)

    while not (is_board_full(board)):
        if not(isWinner(board, 'O')):
            playermove()
            printboard(board)
        else:
            print(' The computer won this game ')
            break

        if not(isWinner(board, 'X')):
            move = compmove()
            if move == 0:
                print('Tie game')
                break
            else:
                insert_letter('O', move)
                print(' Computer placed an \'O\' to position '+str(move))
                printboard(board)

        if is_board_full(board):
            print('Tie game')

while True:
    answer = input('Do you want to play again? (Y/N)')

    if answer.lower() == 'y' or answer.lower() == 'yes':
        board = [' ' for x in range(10)]
        print('----------')
        main()
    else:
        break


