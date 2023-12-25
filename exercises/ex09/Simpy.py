"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union


__author__ = "730645861"


class Simpy:
    """Utility Class."""

    values: list[float]

    def __init__(self, input: list[float]):
        """intializer."""
        self.values: list[float] = input

    def __str__(self) -> str:
        """Outputs string."""
        return f"Simpy({self.values})"

    def fill(self, fl: float, integer: int) -> None:
        """Fills a Simpy's values with a specific number."""
        self.values = []
        counter: int = integer

        while counter > 0:
            self.values.append(fl)
            counter -= 1
        return None

    def arange(self, start: float, stop: float, step: float = 1) -> None:
        """Arranges values."""
        assert step != 0.0
        while (start < stop and step > 0) or (start > stop and step < 0):
            self.values.append(start)
            start += step
        return None

    def sum(self) -> float:
        """Returns the sum of a list."""
        rv: float = sum(self.values)
        return rv

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Adds Simpys together."""
        rl: list = []
        if isinstance(rhs, Simpy): 
            x: int = len(self.values) - 1
            while x >= 0:
                rl.append(self.values[x] + rhs.values[x])
                x -= 1
        else:
            x: int = len(self.values) - 1
            while x >= 0:
                rl.append(self.values[x] + rhs)
                x -= 1
        rl.reverse()
        return Simpy(rl)

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Exponents with Simpys."""
        rl: list = []
        if isinstance(rhs, Simpy): 
            x: int = len(self.values) - 1
            while x >= 0:
                rl.append(self.values[x] ** rhs.values[x])
                x -= 1
        else:
            x: int = len(self.values) - 1
            while x >= 0:
                rl.append(self.values[x] ** rhs)
                x -= 1
        rl.reverse()
        return Simpy(rl)
    
    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the equality of each item."""
        rl: list = []
        if isinstance(rhs, Simpy): 
            x: int = len(self.values) - 1
            while x >= 0:
                if (self.values[x] == rhs.values[x]):
                    rl.append(True)
                else:
                    rl.append(False)
                x -= 1
        else:
            x: int = len(self.values) - 1
            while x >= 0:
                if (self.values[x] == rhs):
                    rl.append(True)
                else:
                    rl.append(False)
                x -= 1
        rl.reverse()
        return Simpy(rl)
    
    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Produces a mask based on the equality of each item."""
        rl: list = []
        if isinstance(rhs, Simpy): 
            x: int = len(self.values) - 1
            while x >= 0:
                if (self.values[x] > rhs.values[x]):
                    rl.append(True)
                else:
                    rl.append(False)
                x -= 1
        else:
            x: int = len(self.values) - 1
            while x >= 0:
                if (self.values[x] > rhs):
                    rl.append(True)
                else:
                    rl.append(False)
                x -= 1
        rl.reverse()
        return Simpy(rl)
    
    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:       
        """Adds the ability to use subscription Notation."""
        rl: list = []
        rl = self.values
        if isinstance(rhs, int):
            rv: int = rl[rhs]
            return rv
        else:
            rlspecial: list = []
            x: int = len(rhs.values) - 1
            while x > 0:
                if (rhs.values[x] is True):
                    rlspecial.append(rl[x])
                x -= 1
            rlspecial.reverse()
            return Simpy(rlspecial)