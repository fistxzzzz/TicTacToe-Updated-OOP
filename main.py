import settings_game.player_set as ps
from settings_game.win_check import WinCheck
from settings_game.play_again import PlayAgainTic

class TicTacToe(WinCheck, ps.Player):
    def __init__(self):
        super().__init__()
        self.set_of_used_nums = []
        self.set_of_used_nums.clear()
        self.cycle_index = 0
    
    def run_game(self):
        self.choose_player()
        if self.game_start_official:
            self.board_num = [' '] * 10
            self.board_display()
        while self.game_start_official:
            set_of_marker = [self.marker1, self.marker2]
            set_ok = {self.marker1:self.x_name, self.marker2:self.y_name}
            player_mark_input = int(input(f"Number to plot {set_ok[set_of_marker[self.cycle_index]].capitalize()} : "))
            if player_mark_input not in range(1,10):
                continue
            if player_mark_input in self.set_of_used_nums:
                print("Can't overlap")
                continue
            self.set_of_used_nums.append(player_mark_input)
            self.board_num[player_mark_input] = set_of_marker[self.cycle_index]
            self.board_display()
            if self.win_win():
                print(f"{set_ok[set_of_marker[self.cycle_index]].capitalize()} WONNN CONGRATSSSSS!!!")
                self.board_num = [' '] * 10
                self.cycle_index = 0
                self.set_of_used_nums.clear()
                PlayAgainTic().q_playagain()


            if len(self.set_of_used_nums) == 9:
                print("All Space Filled!!")
                self.cycle_index = 0
                self.set_of_used_nums.clear()
                self.board_num = [' '] * 10
                PlayAgainTic().q_playagain()

            if self.cycle_index <= 0:
                self.cycle_index += 1
                continue
            self.cycle_index = 0


if __name__ == '__main__':
    x = TicTacToe()
    x.run_game()


 