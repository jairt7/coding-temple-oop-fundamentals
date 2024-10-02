# Practice
# Feel free to ignore this, it's just for my personal reference

class Fighter:
    def __init__(self, hp, attack, speed, name):
        self.hp = hp
        self.attack = attack
        self.speed = speed
        self.name = name
    
    def display_current_stats(self):
        print(f"{self.name} has {self.hp} HP, {self.attack} Attack, and {self.speed} Speed.")
    
    def attacking(self, challenger):
        challenger.hp = challenger.hp - self.attack
        print(f"{challenger.name} now has {challenger.hp} HP")

hp = int(input("How many hit points does your fighter have? "))
attack = int(input("How much damage does your fighter do? "))
speed = int(input("How fast is your fighter? "))
name = input("What should we call your fighter? ")
new_fighter = Fighter(hp, attack, speed, name)
new_challenger = Fighter(10, 12, 8, "Barbie")
new_fighter.display_current_stats()
new_challenger.display_current_stats()
new_fighter.attacking(new_challenger)
new_challenger.display_current_stats()