'''
Lab 26: Tic Tac Toe
'''
import os

class Player:
    def __init__(self,player_name,token):
        self.player_name = player_name
        self.token = token

    def __repr__(self):
        return self.player_name

class Game:
    def __init__(self):
        self.board = [
            [' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' '],
        ]

    def __repr__(self):
        ''' Pretty string representation of the board'''
        return '{0}|{1}|{2}\n{3}|{4}|{5}\n{6}|{7}|{8}'.format(
            self.board[0][0],self.board[0][1],self.board[0][2],
            self.board[1][0],self.board[1][1],self.board[1][2],
            self.board[2][0],self.board[2][1],self.board[2][2],
        )

    def move(self,player):
        ''' Places a player token in the indicated spot'''
        valid_list = list('qweasdzxc')

        while True:
            user_choice = input(f'{player} pick a position to move (q,w,e,a,s,d,z,x,c) > ').lower()
            while user_choice not in valid_list:
                print('Invalid input')
                user_choice = input(f'{player} pick a position to move (q,w,e,a,s,d,z,x,c) > ').lower()

            if user_choice == 'q':
                xy = [0,0]
            elif user_choice == 'w':
                xy = [0,1]
            elif user_choice == 'e':
                xy = [0,2]
            elif user_choice == 'a':
                xy = [1,0]
            elif user_choice == 's':
                xy = [1,1]
            elif user_choice == 'd':
                xy = [1,2]
            elif user_choice == 'z':
                xy = [2,0]
            elif user_choice == 'x':
                xy = [2,1]
            elif user_choice == 'c':
                xy = [2,2]

            if self.board[xy[0]][xy[1]] != ' ':
                print('Space occupied, try again \n')
                continue
            else:
                break

        self.board[xy[0]][xy[1]] = player.token

    def calc_winner(self,player):
        '''Checks  Win scenarios'''
        for x in range(3):
            check_str = ''
            for y in range(3):
                # Checking horizontal wins
                check_str += self.board[x][y]
                if check_str == player.token * 3:
                    print(f'{player.player_name} wins!')
                    return True

        for y in range(3):
            check_str = ''
            for x in range(3):
                # Checking vertical wins
                check_str += self.board[x][y]
                if check_str == player.token * 3:
                    print(f'{player.player_name} wins!')
                    return True

        # Checking Diagonal wins
        if ''.join([self.board[0][0],self.board[1][1],self.board[2][2]]) == (player.token * 3):
            print(f'{player.player_name} wins!')
            return True
        elif ''.join([self.board[0][2],self.board[1][1],self.board[2][0]]) == (player.token * 3):
            print(f'{player.player_name} wins!')
            return True

    def is_full(self):
        ''' Checks for game full scenario '''
        for num in range(3):
            if ' ' in self.board[num]:
                return False
        print('Game board full')
        return True

    def is_game_over(self,player):
        ''' Checks for both game full and game winner scenarios '''
        check_winner = self.calc_winner(player)
        check_full = self.is_full()
        if check_winner != None or check_full == True:
            return True
        else:
            return False

player1 = Player('Player 1','x')
player2 = Player('Player 2','o')
tic_tac_toe = Game()

current_player = player1
def change_player(current_player):
    '''Changes current player'''
    if current_player == player1:
        current_player = player2
    elif current_player == player2:
        current_player = player1
    return current_player

print('Welcome to Tic Tac Toe')
print('\n The game input keys are the following : q,w,e,a,s,d,z,x,c')
print('\n Their relative spaces on the board are the below')
print('\n{q}|{w}|{e}\n{a}|{s}|{d}\n{z}|{x}|{c}')
print(input(f'\n{current_player} Your turn first, press any Key to begin :'))
print(tic_tac_toe)

def main():
    current_player = player1

    while True:
        os.system('clear')
        print(tic_tac_toe)
        tic_tac_toe.move(current_player)
        os.system('clear')
        print(tic_tac_toe)

        check_game_over = tic_tac_toe.is_game_over(current_player)
        if check_game_over == True:
            print('\nGame Over')
            break
        current_player = change_player(current_player)

main()
