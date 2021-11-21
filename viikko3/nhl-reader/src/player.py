class Player:
    def __init__(self, data):
        self.name = data["name"]
        self.nationality = data["nationality"]
        self.team = data["team"]
        self.goals = data["goals"]
        self.assists = data["assists"]
    
    def __str__(self):
        return f"{self.name:20} {self.team} {self.goals} + {self.assists} = {self.goals + self.assists}"

    def __eq__(self, other):
        return self.goals + self.assists == other.goals + other.assists

    def __lt__(self, other):
        return self.goals + self.assists < other.goals + other.assists

    def __gt__(self, other):
        return self.goals + self.assists > other.goals + other.assists
