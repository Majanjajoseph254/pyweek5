# Base class: Character
class Character:
    def __init__(self, name, origin, power_level):
        self.name = name
        self.origin = origin
        self.power_level = power_level

    def introduce(self):
        print(f"Hi, I'm {self.name} from {self.origin}. My power level is {self.power_level}.")

    def boost_power(self, amount):
        self.power_level += amount
        print(f"{self.name}'s power level increased to {self.power_level}!")

# Subclass: Superhero (inherits from Character)
class Superhero(Character):
    def __init__(self, name, origin, power_level, superpower):
        super().__init__(name, origin, power_level)
        self.superpower = superpower

    def use_power(self):
        print(f"{self.name} uses {self.superpower}! 💥")

# Subclass: Villain (inherits from Character)
class Villain(Character):
    def __init__(self, name, origin, power_level, evil_plan):
        super().__init__(name, origin, power_level)
        self.evil_plan = evil_plan

    def scheme(self):
        print(f"{self.name} is plotting: {self.evil_plan} 😈")

# Example usage
hero = Superhero("Nova Blaze", "Solar City", 85, "Solar Flare")
villain = Villain("Shadow Fang", "Dark Realm", 90, "World Domination")

hero.introduce()
hero.use_power()
hero.boost_power(10)

villain.introduce()
villain.scheme()