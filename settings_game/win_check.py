from settings_game.board_tic import Board

class WinCheck(Board):
    def __init__(self):
        super().__init__()

    def win_win(self):
        return (self.board_num[7] == self.board_num[8] == self.board_num[9] == ('X' or 'O') ) or (self.board_num[6] == self.board_num[5] == self.board_num[4] == ('X' or 'O')) or (self.board_num[1] == self.board_num[2] == self.board_num[3] == ('X' or 'O') ) or (self.board_num[7] == self.board_num[6] == self.board_num[1] == ('X' or 'O') ) or (self.board_num[8] == self.board_num[5] == self.board_num[2] == ('X' or 'O') ) or (self.board_num[9] == self.board_num[4] == self.board_num[3] == ('X' or 'O') ) or (self.board_num[7] == self.board_num[5] == self.board_num[3] == ('X' or 'O') ) or (self.board_num[1] == self.board_num[5] == self.board_num[9] == ('X' or 'O') )
