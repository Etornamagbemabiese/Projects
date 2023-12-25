"""File to define Fish class."""
__author__ = "730645861"


class Fish:
    """class for the fishes in the rivers."""
    age: int 

    def __init__(self, age: int = 0):
        """Intializer variables."""
        self.age = age
        return None
    
    def one_day(self):
        """Increments age."""
        self.age += 1
        return None