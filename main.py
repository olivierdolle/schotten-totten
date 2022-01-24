from src import Player, Game

if __name__ == "__main__":
    game = Game()

    player_1 = Player(name="player_1")
    player_2 = Player(name="player_2")
    game.play(player_1, player_2)
