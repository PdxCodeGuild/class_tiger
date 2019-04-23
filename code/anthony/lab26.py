import os
class Board:
    def __init__(self):
        self.board = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]
        self.counter = 0
        self.is_taken = False

    def __repr__(self):
        str_board = ''
        for i in range(len(self.board)):
            str_board += '|'
            for j in range(len(self.board)):
                str_board += self.board[i][j] + '|'
            str_board += '\n'
        return str_board
    
    def check_move(self, x, y, token):
        if self.board[x][y] == ' ':
            self.move(x, y, token)
            return True
        else:
            return False

    def move(self, x, y, token):
        self.board[x][y] = token
        self.counter += 1

    def is_full(self):
        if self.counter >= 9:
            return True

    def is_game_over(self, player):
        if self.calc_winner():
            print(f"Game Over. {player} wins!")
            return True
        
        elif self.is_full():
            print("Game over, the board is full")
            return True
        
        return False
    
    def calc_winner(self):
        current_token = ''
        if self.board[0][0] != ' ': #Top left spot, checks accross, down and diagonal
            current_token = self.board[0][0]
            if self.board[0][1] == current_token:
                if self.board[0][2] == current_token:
                    return True
            if self.board[1][1] == current_token:
                if self.board[2][2] == current_token:
                    return True
            if self.board[1][0] == current_token:
                if self.board[1][2]== current_token:
                    return True
        current_token = ''
        if self.board[0][1] != ' ': #Check top center spot, checks down
            current_token = self.board[0][1]
            if self.board[1][1] == current_token:
                if self.board[2][1] == current_token:
                    return True
        current_token = ''
        if self.board[0][2] != ' ': #Check top right spot, checks down and diagonal
            current_token = self.board[0][2]
            if self.board[1][2] == current_token:
                if self.board[2][2] == current_token:
                    return True
            if self.board[1][1] == current_token:
                if self.board[2][0] == current_token:
                    return True
        current_token = ''
        if self.board[1][0] != ' ': #Check left center spot, checks accross
            current_token = self.board[1][0]
            if self.board[1][1] == current_token:
                if self.board[1][2] == current_token:
                    return True
        current_token = ''
        if self.board[2][0] != ' ': #Check bottom left, checks across
            current_token = self.board[2][0]
            if self.board[2][1] == current_token:
                if self.board[2][2] == current_token:
                    return True




class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

while True:
    new_game = Board()
    game_over = False
    name1 = input("Enter the first players name: ")
    name2 = input("Enter the second players name: ")

    player1 = Player(name1, 'X')
    player2 = Player(name2, 'O')

    while game_over == False:
        if new_game.is_game_over(player1.name) == False:
            x = int(input("Enter the row(1-3): ")) -1
            y = int(input("Enter the column(1-3): ")) -1
            new_game.check_move(x, y, 'X')
            os.system('clear')
            print(new_game)
            if new_game.is_game_over(player1.name) == True:
                game_over = True
                break
        if new_game.is_game_over(player2.name) == False:
            x = int(input("Enter the row(1-3): ")) -1
            y = int(input("Enter the column(1-3): ")) -1
            new_game.check_move(x, y, 'O')
            os.system('clear')
            print(new_game)
            if new_game.is_game_over(player2.name) == True:
                game_over = True
                break
    user_input = input("Would you like to play again? ")
    if user_input != 'yes':
        print("Thank you for playing! ")
        break
        



