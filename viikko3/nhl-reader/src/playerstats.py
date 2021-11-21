from player import Player

class PlayerStats:
    def __init__(self, data):
        self.players = []
        for player_dict in data:
            player = Player(
                player_dict
            )
            self.players.append(player)

    def top_scorers_by_nationality(self, nationality):
        new_list = []
        for player in self.players:
            if player.nationality == nationality:
                new_list.append(player)
        new_list.sort(reverse=True)
        return new_list