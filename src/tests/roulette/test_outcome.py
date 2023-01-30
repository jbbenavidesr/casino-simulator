"""Test cases for the models in the app"""
from casino_simulator.roulette import Outcome


def test_outcome_construction():
    outcome = Outcome("Red", 1)

    assert outcome.name == "Red"
    assert outcome.odds == 1


def test_outcome_equality():
    o1 = Outcome("Red", 1)
    o2 = Outcome("Red", 1)
    o3 = Outcome("Black", 2)
    assert o1 == o2
    assert o1 != o3
    assert o2 != o3


def test_outcome_hash():
    o1 = Outcome("Red", 1)
    o2 = Outcome("Red", 1)
    o3 = Outcome("Black", 2)
    assert hash(o1) == hash(o2)
    assert hash(o1) != hash(o3)
    assert hash(o2) != hash(o3)


def test_outcome_win_amount():
    o1 = Outcome("Red", 1)
    o2 = Outcome("Black", 2)
    assert o1.win_amount(10) == 10
    assert o2.win_amount(10) == 20


def test_outcome_str():
    o1 = Outcome("Red", 1)
    o2 = Outcome("Black", 2)
    assert str(o1) == "Red (1:1)"
    assert str(o2) == "Black (2:1)"


def test_outcome_repr():
    o1 = Outcome("Red", 1)
    o2 = Outcome("Black", 2)
    assert repr(o1) == "Outcome(name='Red', odds=1)"
    assert repr(o2) == "Outcome(name='Black', odds=2)"
