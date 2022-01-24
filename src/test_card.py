from .card import Value


def test_values_can_be_summed():
    assert Value.ONE + Value.TWO == 3
