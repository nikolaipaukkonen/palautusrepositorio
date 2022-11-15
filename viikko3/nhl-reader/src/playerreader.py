import requests
from player import Player

class PlayerReader:
    def __init__(self, url):
        self.players = []
        self.url = url

    def get_players(self):
        response = requests.get(self.url).json()

        for player_dict in response:
            player = Player(
                player_dict["name"], 
                player_dict["nationality"],
                player_dict["assists"],
                player_dict["goals"],
                player_dict["penalties"],
                player_dict["team"],
                player_dict["games"]
            )
            self.players.append(player)

        self.players.sort(reverse=True)

        return self.players