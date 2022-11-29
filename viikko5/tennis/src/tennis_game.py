from player import Player

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)

    def won_point(self, player_name):
        if player_name == self.player1.player_name:
            self.player1.add_score()
        else:
            self.player2.add_score()

    def get_score(self):
        score = ""
        temp_score = 0

        if self.player1.get_score() == self.player2.get_score():
            if self.player1.get_score() == 0:
                score = "Love-All"
            elif self.player1.get_score() == 1:
                score = "Fifteen-All"
            elif self.player1.get_score() == 2:
                score = "Thirty-All"
            elif self.player1.get_score() == 3:
                score = "Forty-All"
            else:
                score = "Deuce"
        elif self.player1.get_score() >= 4 or self.player2.get_score() >= 4:
            minus_result = self.player1.get_score() - self. player2.get_score()

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = self.player1.get_score()
                else:
                    score = score + "-"
                    temp_score = self.player2.get_score()

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"

        return score
