from player_reader import PlayerReader
from statistics import Statistics
from enums.sort_by import SortBy

def main():
    reader = PlayerReader()
    stats = Statistics(reader)
    # philadelphia_flyers_players = stats.team("PHI")
    # top_scorers = stats.top(10)

    # print("Philadelphia Flyers:")
    # for player in philadelphia_flyers_players:
    #     print(player)

    # print("Top point getters:")
    # for player in top_scorers:
    #     print(player)

    print("Top point getters:")
    for player in stats.top(10, SortBy.POINTS):
        print(player)

    # metodi toimii samalla tavalla kuin yo. kutsu myös ilman toista parametria
    for player in stats.top(10):
        print(player)

    # järjestetään maalien perusteella
    print("Top point goal scorers:")
    for player in stats.top(10, SortBy.GOALS):
        print(player)

    # järjestetään syöttöjen perusteella
    print("Top by assists:")
    for player in stats.top(10, SortBy.ASSISTS):
        print(player)

if __name__ == "__main__":
    main()
