"""Tests for the Wheel class.

The idea is to create several Outcomes, add them add them to a couple of Bins in the
Wheel, and test that Wheel instances are appropriately added to the Wheel.

Additionally, we test that the Wheel chooses a Bin at random.
"""
from casino_simulator.roulette import Outcome, Wheel


def test_wheel_construction():
    """Tests that a Wheel instance is created with 38 empty Bins."""
    wheel = Wheel()
    assert len(wheel.bins) == 38
    assert wheel.rng is not None
    for bin in wheel.bins:
        assert len(bin) == 0


def test_wheel_add_outcome():
    """Tests that Outcomes can be added to a Wheel."""
    wheel = Wheel()
    outcome = Outcome("1", 35)
    wheel.add_outcome(1, outcome)
    assert len(wheel.get(1)) == 1
    assert outcome in wheel.get(1)


def test_wheel_choose():
    """Tests that a random Bin is chosen from the Wheel."""
    wheel = Wheel()
    outcome = Outcome("1", 35)
    wheel.add_outcome(7, outcome)
    wheel.rng.seed(42)
    chosen_bin = wheel.choose()
    assert chosen_bin == wheel.get(7)
    assert chosen_bin != wheel.get(2)
