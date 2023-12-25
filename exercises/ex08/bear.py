"""File to define Bear class."""
__author__ = "730645861"


class Bear:
    """Bear class."""
    hunger_score: int
    age: int

    def __init__(self, init_age: int = 0, init_hunger_score: int = 0):
        """Initial variables."""
        self.age = init_age
        self.hunger_score = init_hunger_score
        return None
    
    def one_day(self):
        """Increments age and minuses hunger."""
        self.age += 1
        self.hunger_score -= 1
        return None
    
    def eat(self, num_fish: int):
        """Class for bears to eat."""
        for i in range(0, num_fish):
            self.hunger_score += 1
        return None        
