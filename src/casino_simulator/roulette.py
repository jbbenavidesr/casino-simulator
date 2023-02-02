"""
Roulette simulator.

This module contains the classes that model the game of roulette.
"""
import dataclasses
import random


@dataclasses.dataclass(frozen=True)
class Outcome:
    """Contains a single outcome on which a bet can be placed.

    In Roulette, each spin of the wheel has a number of Outcome objects with bets that
    will be paid off. For example, the “1” bin has the following winning Outcome
    instances:
    “1”, “Red”, “Odd”, “Low”, “Column 1”, “Dozen 1-12”, “Split 1-2”, “Split 1-4”,
    “Street 1-2-3”, “Corner 1-2-4-5”, “Five Bet”, “Line 1-2-3-4-5-6”, “00-0-1-2-3”,
    “Dozen 1”, “Low” and “Column 1”.

    All of thee above-named bets will pay off if the wheel spins a “1”. This makes a
    Wheel and a Bin fairly complex containers of Outcome objects.


    Attributes:
        name (str): Holds the name of the Outcome. Examples include "1" or "Red".
        odds (int): Holds the payout ratio for the Outcome. Most odds are stated as 1:1
            or 17:1, we only keep the numerator(17) and assume the denominator is 1.
    """

    name: str
    odds: int

    def win_amount(self, amount: float) -> float:
        """Multiply this Outcome's odds by the amount bet to determine the amount won.

        Parameters:
            amount (float): The amount bet on this Outcome.

        Returns:
            float: The amount won.
        """
        return amount * self.odds

    def __str__(self) -> str:
        """Easy-to-read string representation of this Outcome."""
        return f"{self.name:s} ({self.odds:d}:1)"


class Bin(set):
    """Represents a bin on the roulette wheel.

    A Bin is a container of Outcome objects. It represents the bins on the wheel, and
    contains all of the winning Outcomes for a given spin of the wheel where the ball
    lands in that bin.

    For example, the "1" bin contains the following Outcomes:
    "1", "Red", "Odd", "Low", "Column 1", "Dozen 1-12", "Split 1-2", "Split 1-4",
    "Street 1-2-3", "Corner 1-2-4-5", "Five Bet", "Line 1-2-3-4-5-6", "00-0-1-2-3",
    "Dozen 1", "Low" and "Column 1". All of these Outcomes are collected in a single
    Bin instance representing the "1" bin.

    The following code shows how to create a Bin instance containing the "0" and "00"
    bins and their associated Outcomes:

    .. code-block:: python

        five = Outcome("00-0-1-2-3", 6)
        zero = Bin([Outcome("0", 35), five])
        zerozero = Bin([Outcome("00", 35), five])


    .. note::
        This class is a subclass of frozenset. This means that it allows no duplicates,
        has no order, and is immutable. This is a good choice for a Bin because it
        should never change after it is created. It is also a good choice because it
        allows no duplicates, which is important because a Bin should never contain
        duplicate Outcomes.
    """


class Wheel:
    """Represents a roulette wheel.

    The wheel contains the 38 individual Bins that make up the wheel and a random number
    generator. It selects a Bin at random, simulating the spinning of a roulette wheel.

    Attributes:
        rng (random.Random): A random number generator.
        bins (tuple[Bin]): A list of 38 Bins.
    """

    def __init__(self) -> None:
        """Creates a new Wheel instance with 38 empty Bins and a new random generator"""
        self.bins = tuple(Bin() for _ in range(38))
        self.rng = random.Random()

    def add_outcome(self, bin_number: int, outcome: Outcome) -> None:
        """Adds an Outcome to the Bin at the given index.

        Parameters:
            bin_number (int): The index of the Bin to add the Outcome to.
            outcome (Outcome): The Outcome to add to the Bin.
        """
        self.bins[bin_number].add(outcome)

    def choose(self) -> Bin:
        """Selects a Bin at random and returns it.

        Returns:
            Bin: A random Bin.
        """
        return self.rng.choice(self.bins)

    def get(self, bin_number: int) -> Bin:
        """Returns the Bin at the given index.

        Parameters:
            bin_number (int): The index of the Bin to return.

        Returns:
            Bin: The Bin at the given index.
        """
        return self.bins[bin_number]
