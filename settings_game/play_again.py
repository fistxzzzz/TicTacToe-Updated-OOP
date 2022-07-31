from settings_game.player_set import Player

class PlayAgainTic(Player):
    def __init__(self):
        super().__init__()

    def q_playagain(self):
        question_playagain = input("Do you Want to Play again? : ")
        if question_playagain.lower() == 'y':
            self.choose_player()
        else:
            print("Thanks for playing!")
            quit()


# IN PROGRESS