from dataclasses import dataclass
from enum import IntEnum
from .color import Color


class Value(IntEnum):
    ZERO = 0  # Default
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9


@dataclass
class Card:
    color: Color = Color.NULL
    value: Value = Value.ZERO

    def __eq__(self, other) -> bool:
        return self.value == other.value and self.color == other.color

    def __lt__(self, other: "Card") -> bool:
        return self.value < other.value

    def __gt__(self, other: "Card") -> bool:
        return self.value > other.value

    def get_state(self) -> tuple[int, int]:
        """State representation"""
        return (self.color.value, self.value.value)
