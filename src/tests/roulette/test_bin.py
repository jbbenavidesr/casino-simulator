"""Tests for the Bin class."""
from casino_simulator.roulette import Bin, Outcome


def test_bin_construction():
    """Test that a Bin can be constructed."""
    bin = Bin()
    assert bin is not None
    assert len(bin) == 0


def test_bin_constructor_with_outcomes():
    """Test that a Bin can be constructed with a list of Outcomes."""
    five = Outcome("00-0-1-2-3", 6)
    bin = Bin([Outcome("00", 35), five])
    assert len(bin) == 2
    assert Outcome("00", 35) in bin
    assert five in bin
