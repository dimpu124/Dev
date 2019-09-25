from IPython.display import clear_output
def display_board(board):
    clear_output()
    print(f'{board[9]} | {board[8]} | {board[7]} \n{board[4]} | {board[5]} | {board[6]} \n{board[1]} | {board[2]} | {board[3]}')


#display_board(test_board)

def player_input():
    player1=''
    while not (player1=='X' or player1=='O'):
        player1=input('Player 1: Do you want to be X or O? ').upper()

    if player1 == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')

def place_marker(board, marker, position):
    board[position]=marker
    return board

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal
    

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'

def space_check(board, position):
    if board[position]==' ':
        return True
    else:
        return False
    
def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
        
    return position

def replay():
    s=input("Do you want to play again Y or N")
    if s=='Y':
        return True
    else:
        return False
        
        
        

print('Welcome to Tic Tac Toe!') 
while True:
    board=[' ']*10
    (p1,p2)=player_input()
    turn=choose_first()
    print(turn +' Will go First')
    play_game = input('Are you ready to play? Enter Yes or No.')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False
    
    while game_on:
        if turn=='Player 1':
            display_board(board)
            position = player_choice(board)
            place_marker(board, p1, position)
            if win_check(board,p1):
                display_board(board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'
        else:
            display_board(board)
            position = player_choice(board)
            place_marker(board, p2, position)

            if win_check(board, p2):
                display_board(board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(board):
                    display_board(board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
            
                
                
            



    

