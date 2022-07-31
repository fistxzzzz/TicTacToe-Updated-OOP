from settings_game.board_tic import Board

class Player(Board):
    def __init__(self):
        super().__init__()
        self.marker1 = 'X'
        self.marker2 = 'O'
        self.x_name = ''
        self.y_name = ''
        self.game_start_official = True
    
    def choose_player(self):
        self.board_display()
        print("Now, We gotta choose our markers Either 'X' or 'O' \nPlayer 1 gets 'X' while Player 2 gets 'O'")
        while self.x_name == '':
            self.x_name = input("Enter the name of the first player who wants to play 'X' : ")
        print(f"Welcome!, {self.x_name.capitalize()} 'X' ")
        while self.y_name == '':
            self.y_name = input("Enter the name of the second player who wants to play 'Y' : ")
        print(f"Welcome!, {self.y_name.capitalize()} 'O' ")
        self.board_display()
        print("Please Go through the numbers of this board and type 'y' when ready or 'q' to quit")
        game_start_req = str()
        while game_start_req.lower() not in ['y', 'q']:
            game_start_req = input()
        if game_start_req.lower() == 'y':
            self.game_start_official = True
        elif game_start_req.lower() == 'q':
            quit()