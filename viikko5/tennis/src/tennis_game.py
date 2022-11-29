from player import Player
from score_service import ScoreService

class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = Player(player1_name)
        self.player2 = Player(player2_name)
        self.score_service = ScoreService()

    def won_point(self, player_name):
        if player_name == self.player1.player_name:
            self.player1.add_score()
        else:
            self.player2.add_score()

    def get_score(self):
        return self.score_service.compare_scores(self.player1.get_score(), self.player2.get_score())
        
