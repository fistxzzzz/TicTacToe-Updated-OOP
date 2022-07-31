

class Board:
    def __init__(self):
        self.board_num = ['N', '1','2','3','4','5','6','7','8','9']
        self.set_of_used_nums = []

    def board_display(self):
        print(f"  {self.board_num[7]}   |  {self.board_num[8]}   |   {self.board_num[9]}  ")

        print(f"------+------+------")

        print(f"  {self.board_num[6]}   |  {self.board_num[5]}   |   {self.board_num[4]}  ")

        print(f"------+------+------")

        print(f"  {self.board_num[1]}   |  {self.board_num[2]}   |   {self.board_num[3]}  ")


