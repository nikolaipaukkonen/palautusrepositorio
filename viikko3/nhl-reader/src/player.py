class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def points(self):
        return self.assists + self.goals
    
    def __str__(self):
        points = self.assists + self.goals
        return f'{self.name:<25} {self.team} {self.goals:>2} + {self.assists:<2} = {points}'