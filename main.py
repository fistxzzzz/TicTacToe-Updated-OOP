import settings_game.player_set as ps

class TicTacToe(ps.Player):
    def __init__(self):
        super().__init__()
    
    def run_game(self):
        self.choose_player()
        if self.game_start_official:
            self.board_num = [' '] * 10
            self.board_display()
            cycle_index = 0
            set_of_used_nums = []
        while self.game_start_official:
            set_of_marker = [self.marker1, self.marker2]
            player_mark_input = int(input("Number to plot : "))
            if player_mark_input in set_of_used_nums:
                print("Cant overlap")
                continue
            set_of_used_nums.append(player_mark_input)
            self.board_num[player_mark_input] = set_of_marker[cycle_index]
            self.board_display()

            if cycle_index <= 0:
                cycle_index += 1
                continue
            cycle_index = 0


if __name__ == '__main__':
    x = TicTacToe()
    x.run_game()


 