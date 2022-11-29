class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player_name):
        if player_name == "player1":
            self.m_score1 = self.m_score1 + 1
        else:
            self.m_score2 = self.m_score2 + 1

    def get_score(self):
        score = ""
        temp_score = 0

        def getTiedScore():
            possible_scores = {
                        0: "Love-All",
                        1: "Fifteen-All",
                        2: "Thirty-All",
                        3: "Forty-All",
                    }
            return possible_scores.get(self.m_score1, "Deuce")

        def getBrakePointScore():
            difference = self.m_score1 - self. m_score2
            outcome = "Advantage " if abs(difference) == 1 else "Win for "
            player = "player1" if difference > 0 else "player2"
            return outcome + player

        def getGameScore():
            possible_scores = {
                        0: "Love",
                        1: "Fifteen",
                        2: "Thirty",
                        3: "Forty",
                    }
            return f"{possible_scores[self.m_score1]}-{possible_scores[self.m_score2]}"

        if self.m_score1 == self.m_score2:
            score = getTiedScore()
        elif max(self.m_score1, self.m_score2) >= 4:
            score = getBrakePointScore()
        else:
            score = getGameScore()

        return score
