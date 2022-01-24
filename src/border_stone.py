from typing import Optional

from .card import Card
from .triplet import build_triplet


class BorderStone:
    def __init__(self):
        self.player_1: list[Card] = []
        self.player_2: list[Card] = []
        self.owner = None
        self.__first_to_3_cards = None

    def can_add_card(self, player) -> bool:
        current_player = getattr(self, player, None)
        if current_player is None:
            raise ValueError(f"Player {player} does not exist")

        return len(current_player) < 3

    def add_card(self, player: str, card: Card) -> Optional[str]:
        if self.can_add_card(player):
            getattr(self, player).append(card)
        else:
            raise ValueError("Bad move")

        if len(getattr(self, player)) == 3 and self.__first_to_3_cards is None:
            self.__first_to_3_cards = player

        if len(self.player_1) == 3 and len(self.player_2) == 3:
            triplet_player_1 = build_triplet(self.player_1)
            triplet_player_2 = build_triplet(self.player_2)

            if triplet_player_1 > triplet_player_2:
                self.owner = "player_1"
            elif triplet_player_2 > triplet_player_1:
                self.owner = "player_2"
            else:
                self.owner = self.__first_to_3_cards

            return self.owner

        return None

    def get_state(self, player: str) -> list[tuple[int, int]]:
        """ "Return the border stone state as a single list with:
        - the player's cards last
        - card are sorted from lowest to hightest for the current player
        - reverse order for the enemy
        - 0 padded to reach three cards each
        e.g.
        [0, 22, 23, 54, 44, 0]
        """
        if player == "player_1":
            return _players_cards_to_state(self.player_1, self.player_2)
        return _players_cards_to_state(self.player_2, self.player_1)


def _players_cards_to_state(
    cards_current_player: list[Card], cards_adversary: list[Card]
) -> list[tuple[int, int]]:
    cards_current_player_state = _cards_to_state(cards_current_player)
    cards_adversary_state = _cards_to_state(cards_adversary)

    return cards_adversary_state + cards_current_player_state[::-1]


def _cards_to_state(cards: list[Card]) -> list[tuple[int, int]]:
    """
    - Convert each card to its state representation
    - Pad with "default" cards up to three cards max
    - Sort
    """
    return [c.get_state() for c in sorted(cards + [Card()] * (3 - len(cards)))]
