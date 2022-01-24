from random import shuffle
from typing import Optional

from .card import Card, Value
from .color import Color


class Deck:
    def __init__(self):
        self.cards = self.__build()

    @staticmethod
    def __build() -> list[Card]:
        cards = [
            Card(color, value)
            for color in Color
            if color != Color.NULL
            for value in Value
            if value != Value.ZERO
        ]

        shuffle(cards)
        print(f"Number of cards in deck: {len(cards)}")
        return cards

    def draw(self) -> Optional[Card]:
        if len(self.cards) > 0:
            return self.cards.pop()

        return None

    def __len__(self) -> int:
        return len(self.cards)
