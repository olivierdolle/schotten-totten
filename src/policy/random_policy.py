from random import choice

import numpy as np

from ..card import Card


class RandomPolicy:
    def __init__(self):
        # no state to instantiate
        pass

    @staticmethod
    def apply(hand: list[Card], state: np.ndarray) -> tuple[Card, int]:
        card = choice(hand)
        hand.remove(card)

        playable_columns = RandomPolicy.get_playable_columns(state)
        column = choice(playable_columns)

        return card, column

    @staticmethod
    def get_playable_columns(state: np.ndarray) -> list[int]:
        return [i for i, value in enumerate(state[0, 5, :]) if value == 0]
