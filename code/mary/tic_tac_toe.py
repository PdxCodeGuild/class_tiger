#tic_tac_toe.py

class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return self.token

class Game:
    def __init__(self):
        self.board = (
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "]
        )

    def __repr__(self):
        grid = ''
        for row in self.board:
            grid += '|'.join(row)
            grid += '\n'
        return grid

    def move(x, y, player):
        if self.board[y][x] == token:
            return token
        elif self.board[y][x] == ' ':
            return("Space already taken")

    def calc_winner(self):




    def is_full(self):
        if self.board != " ":
            return True


    def is_game_over(self):
        return self.calc_winner() or self.is_full()

game = Game()
def main(game):
    while True:
        p1 = input("Player one, please enter your name: ")
        p1 = 'X'
        p2 = input("player two, please enter your name: ")
        p2 = 'O'













main(game)
