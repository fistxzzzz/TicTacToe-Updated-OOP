from board_tic import Board
import time

class Player(Board):
    def __init__(self):
        super().__init__()
        self.marker1 = 'X'
        self.marker2 = 'O'
        self.x_name = ''
        self.y_name = ''
    
    def choose_player(self):
        self.board_display()
        print("Now, We gotta choose our markers Either 'X' or 'O' \nPlayer 1 gets 'X' while Player 2 gets 'O'")
        while self.x_name == '':
            self.x_name = input("Enter the name of the first player who wants to play 'X' : ")
        print(f"Welcome!, {self.x_name.capitalize()} 'X' ")
        time.sleep(2)
        while self.y_name == '':
            self.y_name = input("Enter the name of the second player who wants to play 'Y' : ")
        print(f"Welcome!, {self.y_name.capitalize()} 'O' ")