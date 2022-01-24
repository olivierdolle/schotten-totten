from dataclasses import dataclass, field

from .card import Card
from .policy import RandomPolicy


@dataclass
class Player:
    name: str
    cards: list[Card] = field(default_factory=list)
    policy: RandomPolicy = RandomPolicy()

    def get_move(self, state):
        return self.policy.apply(self.cards, state)
