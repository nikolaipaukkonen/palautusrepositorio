from playerreader import PlayerReader

class PlayerStats:
    def __init__(self, reader: PlayerReader):
        self.reader = reader

    def top_scorers_by_nationality(self, nationality: str):
        players = self.reader.get_players()
        return_list = []

        for player in players:
            if player.nationality == nationality:
                return_list.append(player)
                
        return_list.sort(reverse=True)
        return return_list