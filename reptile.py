# create a class called Reptile - To inherit from Animal class
from animal import Animal


class Reptile(Animal):  # Inherit from Animal class
    def __init__(self):
        super().__init__()  # Used to inherit everything from the parent class
        self.cold_blooded = True
        self.tetrapods = None
        self.heart_chambers = [3, 4]

    def hunt(self):
        return "keep working hard to find food! "

    def use_venom(self):
        return "if i have it, i will use it"


# Implementing Inheritance
smart_reptile = Reptile()
print(smart_reptile.breathe())
print(smart_reptile.hunt())
