import settings_game.player_set as ps

class TicTacToe(ps.Player):
    def __init__(self):
        super().__init__()
    
    def run_game(self):
        self.choose_player()


if __name__ == '__main__':
    x = TicTacToe()
    x.run_game()


 