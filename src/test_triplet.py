import pytest

from .card import Card, Value
from .color import Color
from .triplet import build_triplet, Figure, Triplet


def test_figures_are_comparable():
    assert isinstance(Figure.COLOR > Figure.NULL, bool)


@pytest.mark.parametrize(
    "cards, expected_triplet",
    (
        (
            [
                Card(color=Color.RED, value=Value.ONE),
                Card(color=Color.RED, value=Value.TWO),
                Card(color=Color.RED, value=Value.THREE),
            ],
            Triplet(total=6, figure=Figure.FLUSH),
        ),
        (
            [
                Card(color=Color.RED, value=Value.ONE),
                Card(color=Color.YELLOW, value=Value.TWO),
                Card(color=Color.BLUE, value=Value.THREE),
            ],
            Triplet(total=6, figure=Figure.SUITE),
        ),
        (
            [
                Card(color=Color.RED, value=Value.ONE),
                Card(color=Color.YELLOW, value=Value.TWO),
                Card(color=Color.BLUE, value=Value.FOUR),
            ],
            Triplet(total=7, figure=Figure.NULL),
        ),
        (
            [
                Card(color=Color.RED, value=Value.ONE),
                Card(color=Color.YELLOW, value=Value.ONE),
                Card(color=Color.BLUE, value=Value.ONE),
            ],
            Triplet(total=3, figure=Figure.TRIPLE),
        ),
        (
            [
                Card(color=Color.RED, value=Value.ONE),
                Card(color=Color.RED, value=Value.TWO),
                Card(color=Color.RED, value=Value.FOUR),
            ],
            Triplet(total=7, figure=Figure.COLOR),
        ),
    ),
)
def test_build_triplet(cards, expected_triplet):
    assert build_triplet(cards) == expected_triplet


@pytest.mark.parametrize(
    "hand1, hand2",
    (
        (
            Triplet(6, Figure.FLUSH),
            Triplet(3, Figure.TRIPLE),
        ),
        (Triplet(3, Figure.TRIPLE), Triplet(7, Figure.COLOR)),
        (
            Triplet(3, Figure.COLOR),
            Triplet(7, Figure.SUITE),
        ),
        (
            Triplet(3, Figure.SUITE),
            Triplet(7, Figure.NULL),
        ),
        (
            # Same Figure, but distinct total
            Triplet(9, Figure.FLUSH),
            Triplet(6, Figure.FLUSH),
        ),
    ),
)
def test_hand_superiority(hand1, hand2):
    assert hand1 > hand2


@pytest.mark.parametrize(
    "hand1, hand2",
    (
        (Triplet(9, Figure.FLUSH), Triplet(9, Figure.FLUSH)),
        (
            Triplet(9, Figure.NULL),
            Triplet(9, Figure.NULL),
        ),
    ),
)
def test_hand_equality(hand1, hand2):
    assert hand1 == hand2
