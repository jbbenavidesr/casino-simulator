"""
Roulette simulator.

This module contains the classes that model the game of roulette.
"""
import dataclasses


@dataclasses.dataclass(frozen=True)
class Outcome:
    """Outcome contains a single outcome on which a bet can be placed.

    In Roulette, each spin of the wheel has a number of Outcome objects with bets that
    will be paid off. For example, the “1” bin has the following winning Outcome instances:
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
