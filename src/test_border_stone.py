import pytest

from .border_stone import _cards_to_state, _players_cards_to_state
from .card import Card, Value
from .color import Color


@pytest.mark.parametrize(
    "cards, expected",
    (
        ([], [(0, 0)] * 3),
        (
            [Card(color=Color.BLUE, value=Value.ONE)],
            [(0, 0)] * 2 + [Card(color=Color.BLUE, value=Value.ONE).get_state()],
        ),
        (
            [
                Card(color=Color.BLUE, value=Value.NINE),
                Card(color=Color.BLUE, value=Value.ONE),
            ],
            [
                (0, 0),
                Card(color=Color.BLUE, value=Value.ONE).get_state(),
                Card(color=Color.BLUE, value=Value.NINE).get_state(),
            ],
        ),
        (
            [
                Card(color=Color.BLUE, value=Value.NINE),
                Card(color=Color.BLUE, value=Value.ONE),
                Card(color=Color.RED, value=Value.EIGHT),
            ],
            [
                Card(color=Color.BLUE, value=Value.ONE).get_state(),
                Card(color=Color.RED, value=Value.EIGHT).get_state(),
                Card(color=Color.BLUE, value=Value.NINE).get_state(),
            ],
        ),
    ),
)
def test_cards_to_state(cards, expected):
    assert _cards_to_state(cards) == expected


@pytest.mark.parametrize(
    "player_current, player_adversary, expected",
    (
        ([], [], [(0, 0)] * 6),
        (
            [Card(color=Color.BLUE, value=Value.ONE)],
            [],
            [(0, 0)] * 3
            + [Card(color=Color.BLUE, value=Value.ONE).get_state()]
            + [(0, 0)] * 2,
        ),
        (
            [Card(color=Color.BLUE, value=Value.ONE)],
            [Card(color=Color.RED, value=Value.NINE)],
            [(0, 0)] * 2
            + [
                Card(color=Color.RED, value=Value.NINE).get_state(),
                Card(color=Color.BLUE, value=Value.ONE).get_state(),
            ]
            + [(0, 0)] * 2,
        ),
    ),
)
def test_players_cards_to_state(player_current, player_adversary, expected):
    assert _players_cards_to_state(player_current, player_adversary) == expected
