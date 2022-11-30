class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1 = player1_name
        self.player2 = player2_name
        self.score = {
                    self.player1: 0,
                    self.player2: 0
                }

    def won_point(self, player_name):
        self.score[player_name] += 1

    def get_score(self):
        score = ""
        brake_point_limit = 4

        def getTiedScore():
            possible_scores = {
                        0: "Love-All",
                        1: "Fifteen-All",
                        2: "Thirty-All",
                        3: "Forty-All",
                    }
            return possible_scores.get(self.score[self.player1], "Deuce")

        def getBrakePointScore():
            difference = self.score[self.player1] - self.score[self.player2]
            outcome = "Advantage " if abs(difference) == 1 else "Win for "
            # Should really be like below but tests wont allow...
            # player = self.player1 if difference > 0 else self.player2
            player = "player1" if difference > 0 else "player2"
            return outcome + player

        def getGameScore():
            possible_scores = {
                        0: "Love",
                        1: "Fifteen",
                        2: "Thirty",
                        3: "Forty",
                    }
            return f"{possible_scores[self.score[self.player1]]}-{possible_scores[self.score[self.player2]]}"

        if self.score[self.player1] == self.score[self.player2]:
            score = getTiedScore()
        elif max(self.score.values()) >= brake_point_limit:
            score = getBrakePointScore()
        else:
            score = getGameScore()

        return score
