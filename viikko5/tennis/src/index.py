from tennis_game import TennisGame


def main():
    game = TennisGame("Federer", "Williams")

    print(game.get_score())

    game.won_point("Federer")
    print(game.get_score())

    game.won_point("Federer")
    print(game.get_score())

    game.won_point("Williams")
    print(game.get_score())

    game.won_point("Federer")
    print(game.get_score())

    game.won_point("Federer")
    print(game.get_score())


if __name__ == "__main__":
    main()
