class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        score = ""

        if self.player1_score == self.player2_score:
            score = self.get_even_score()
        elif self.player1_score >= 4 or self.player2_score >= 4:
            score = self.get_advantageous_score()
        else:
            score = self.get_other_score()

        return score

    def get_even_score(self):
        scores = {
            0: "Love-All",
            1: "Fifteen-All",
            2: "Thirty-All",
            3: "Forty-All"
        }
        if self.player1_score in scores:
            return scores[self.player1_score]
        return "Deuce"

    def get_advantageous_score(self):
        minus_result = self.player1_score - self. player2_score

        if minus_result == 1:
            return "Advantage player1"
        elif minus_result == -1:
            return "Advantage player2"
        elif minus_result >= 2:
            return "Win for player1"
        return "Win for player2"

    def get_other_score(self):
        scores = {
            0: "Love",
            1: "Fifteen",
            2: "Thirty",
            3: "Forty"
        }
        return f"{scores[self.player1_score]}-{scores[self.player2_score]}"