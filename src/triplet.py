from dataclasses import dataclass
from enum import IntEnum
from typing import List

from .card import Card


class Figure(IntEnum):
    NULL = 0
    SUITE = 1
    COLOR = 2
    TRIPLE = 3
    FLUSH = 4


@dataclass
class Triplet:
    total: int
    figure: Figure

    def __eq__(self, other):
        return self.figure == other.figure and self.total == other.total

    def __lt__(self, other):
        return self.figure < other.figure or (
            self.figure == other.figure and self.total < other.total
        )

    def __gt__(self, other):
        return self.figure > other.figure or (
            self.figure == other.figure and self.total > other.total
        )


def build_triplet(cards: List[Card]) -> Triplet:
    cards_ = sorted(cards)

    total = sum(card.value for card in cards_)

    if all(card.value == cards_[0].value for card in cards_):
        return Triplet(total, Figure.TRIPLE)

    if all(card.color == cards_[0].color for card in cards_):
        if (cards_[2].value - cards[1].value == 1) and (
            cards_[1].value - cards_[0].value == 1
        ):
            return Triplet(total, Figure.FLUSH)

        return Triplet(total, Figure.COLOR)

    if (cards_[2].value - cards[1].value == 1) and (
        cards_[1].value - cards_[0].value == 1
    ):
        return Triplet(total, Figure.SUITE)

    return Triplet(total, Figure.NULL)
