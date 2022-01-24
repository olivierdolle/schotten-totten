from typing import Optional, Union

import numpy as np

from .border_stone import BorderStone
from .card import Card
from .deck import Deck
from .player import Player


class Game:
    def __init__(self):
        self.border_stones = [BorderStone() for _ in range(9)]
        self.deck = Deck()

    def play(self, player_1: Player, player_2: Player):
        print("Starting a new game")
        for i in range(2 * 6):
            card = self.deck.draw()

            if i % 2 == 0:
                player_1.cards.append(card)
            else:
                player_2.cards.append(card)

        winner = None
        current_player = player_1
        while winner is None:
            state = self.get_state(current_player.name)
            card, column = current_player.get_move(state)

            print(f"{current_player.name.title()} plays {card} in column {column}")

            if self.is_valid_move(current_player.name, column):
                new_card = self.step(current_player.name, card, column)
            else:
                continue

            if isinstance(new_card, str):
                winner = new_card
            elif new_card is not None:
                current_player.cards.append(new_card)

            current_player = player_2 if current_player == player_1 else player_1

        print(self.get_state(current_player.name))
        print(f"End of game, winner: {winner}")

    def is_valid_move(self, player: str, column) -> bool:
        return self.border_stones[column].can_add_card(player)

    def step(
        self, player: str, card: Card, stone_index: int
    ) -> Optional[Union[Card, str]]:
        owner = self.border_stones[stone_index].add_card(player, card)

        if owner is not None:
            print(f"{player.title()} owns border stone {stone_index}")
            # Check for victory
            # either 3 consecutives border stones owned by a player
            # or a total of 5
            stone_ownership = [
                s.owner if s.owner is not None else "None" for s in self.border_stones
            ]

            if stone_ownership.count("player_1") == 5:
                print("Player 1 wins")
                print("|".join(stone_ownership))
                return "player_1"

            if stone_ownership.count("player_2") == 5:
                print("Player 11 wins")
                print("|".join(stone_ownership))
                return "player_2"

            consecutive_3 = list(
                zip(
                    stone_ownership[:-2],
                    stone_ownership[1:-1],
                    stone_ownership[2:],
                )
            )

            if ("player_1",) * 3 in consecutive_3:
                print("|".join(stone_ownership))
                return "player_1"

            if ("player_2",) * 3 in consecutive_3:
                print("|".join(stone_ownership))
                return "player_2"

            print("No winner yet")

        return self.deck.draw()

    def get_state(self, player: str) -> np.ndarray:
        """Return a representation of the cards on the board as
        Adversary board
        | 21 |  0 | ...
        | 22 |  0 | ...
        | 23 |  0 | ...

        | 19 | 49 | ...
        | 39 |  0 | ...
        |  0 |  0 | ...
        player's board
        """
        state = [border_stone.get_state(player) for border_stone in self.border_stones]

        return np.asarray(state, dtype=np.int8).transpose()
