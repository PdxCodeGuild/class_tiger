import os

class Game:
    def __init__(self, player, token):
        self.game_board = [
            [" ", " ", " "],
            [" ", " ", " "],
            [" ", " ", " "]
        ]
        self.player = player
        self.token = token
        self.winner = False
        self.full_board = False
        
    def move(self, player, x, y):
        x = int(x)
        y = int(y)
        y = self.game_board[y-1]
        if y[x-1] != " ":
            y = input("Token already in this space. Try again\nWhich row? ")
            x = input('Which colomn? ')
            x = int(x)
            y = int(y)
            y = self.game_board[y-1]
        # x = y[x-1]
        y[x-1] = player.token
        os.system('clear')
        return self.game_board

    def check_winner(self):
        for i in range(3):
            if self.game_board[i][1] != " ":
                if self.game_board[i][0] == self.game_board[i][1] and self.game_board[i][1] == self.game_board[i][2]:
                    self.winner = True
                    return self.winner
            elif self.game_board[i][1] != " ":
                if self.game_board[0][i] == self.game_board[1][j] and self.game_board[1][j] == self.game_board[2][j]:
                    self.winner = True
                    return self.winner
        if self.game_board[1][1] != " ":
            if self.game_board[0][0] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][2]:
                self.winner = True
                return self.winner
            elif self.game_board[0][2] == self.game_board[1][1] and self.game_board[1][1] == self.game_board[2][2]:
                self.winner = True
                return self.winner
        else:
            self.winner = False
            return self.winner

    def full(self):
        counter = 0
        for i in range(3):
            for j in range(3):
                counter =+ 1
                if self.game_board[i][j] == " ":
                    self.full_board = False
                elif counter < 9:
                    self.full_board = False
                else:
                    self.full_board = True
        return self.full_board

    def over(self, player):
        if self.check_winner() == True:
            return player.name + " won!"
        if self.full() == True:
            return "Game Over"
        else:
            return False


    def __repr__(self):
        return '\n{} | {} | {}\n{} | {} | {}\n{} | {} | {}\n'.format(
            self.game_board[0][0],
            self.game_board[0][1],
            self.game_board[0][2],
            self.game_board[1][0],
            self.game_board[1][1],
            self.game_board[1][2],
            self.game_board[2][0],
            self.game_board[2][1],
            self.game_board[2][2]
            )


class Player:
    def __init__(self, name, token):
        self.name = name
        self.token = token

    def __repr__(self):
        return 'Player({!r}, {!r})'.format(
            self.name,
            self.token
        )

def main():
    p1_name = input("Player 1 name: ")
    p2_name = input("Player 2 name: ")
    player1 = Player(p1_name, "X")
    player2 = Player(p2_name, "O")
    os.system('clear')
    token = " "
    x = 0
    y = 0
    play = Game(player1, token)
    print(play)
    while True:
        name = p1_name
        y = input(f"--{name}--\nwhich row? ")
        x = input("which colomn? ")
        play.move(player1, x, y)
        if play.over(player1):
            print(play.over(player1))
            break
        print(play)
        name = p2_name
        y = input(f"--{name}--\nwhich row? ")
        x = input("which colomn? ")
        play.move(player2, x, y)
        if play.over(player2):
            print(play.over(player2))
            break
        print(play)


main()