class Player:
    def __init__(self, name:str, nationality:str, team:str, stats:dict):
        self.name = name
        self.nationality = nationality
        self.team = team
        self.stats = stats

    def __gt__(self, other):
        return self.name > other.name
    
    def __str__(self):
        return self.name

    def __repr__(self):
        return (f"{self.name} ({self.nationality}, {self.team})"
                f"(goals:{self.stats['goals']}, assists:{self.stats['assists']}, "
                f"games:{self.stats['games']}, penalties:{self.stats['penalties']})")
