"""File to define River class."""
__author__ = "730645861"

from exercises.ex08.fish import Fish
from exercises.ex08.bear import Bear


class River:
    """River Class that imports fish and bear class to create an ecosystem."""

    day: int 
    bears: list 
    fish: list
    
    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears."""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for x in range(0, num_fish):
            self.fish.append(Fish())
        for x in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        """Function checks the ages."""
        survivf: list[Fish] = []
        survivb: list[Bear] = []
        for i in self.fish:
            if i.age <= 3:
                survivf.append(i)
        for i in self.bears:
            if i.age <= 5:
                survivb.append(i)
        self.fish = survivf
        self.bears = survivb
        return None

    def bears_eating(self):
        """Bears eating."""
        for e in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                e.eat(3)
        return None
    
    def check_hunger(self):
        """Check hunger."""
        b: list[Bear] = []
        for i in self.bears:
            if i.hunger_score >= 0:
                b.append(i)
        self.bears = b
        return None
        
    def repopulate_fish(self):
        """Repopulates fish."""
        c: int = (len(self.fish) // 2) * 4
        for i in range(0, c):
            self.fish.append(Fish())
        return None
    
    def repopulate_bears(self):
        """Repopulates bears."""
        c: int = (len(self.bears) // 2)
        for i in range(0, c):
            self.bears.append(Bear())
        return None
    
    def view_river(self):
        """Prints the river."""
        print(f"~~~ Day {self.day}: ~~~  \n Fish population: {len(self.fish)} \n Bear population: {len(self.bears)}")
        return None
            
    def one_river_day(self):
        """Simulate one day of life in the river."""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        """Simulates a week at the river."""
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        self.one_river_day()
        return None

    def remove_fish(self, amount: int):
        """Removing fish."""
        for i in range(0, amount):
            self.fish.pop(0)        
        return None