class Player:
    def __init__(self, name:str, nationality:str, team:str, assists:int, goals:int, penalties:int, games:int):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.stats = {}
        self.stats['assists'] = assists
        self.stats['goals'] = goals
        self.stats['penalties'] = penalties
        self.stats['games'] = games

    def points(self):
        return self.stats['goals'] + self.stats['assists']

    def __gt__(self, other):
        return self.name > other.name
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return (f"{self.name : <25}{self.team : <4}{self.stats['goals'] : >3}  "
                f"+{self.stats['assists'] : >3}  ={self.points() : >3}")
