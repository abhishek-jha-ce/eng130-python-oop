# create a class called Animal - file-name is lowercase - class-name is Capitalized
# add the common attributes/var and behaviour/functions
# Syntax class Name:  e.g. class Animal:

class Animal:
    def __init__(self):  # Initialise the class with built-in method called __init__(self)
        self.alive = True
        self.spine = True
        self.eyes = True

    # let's create some methods to add common behaviour
    def breathe(self):
        return "Keep breathing to stay alive"

    def eat(self):
        return "Time to eat"


# Create an object of this class
cat = Animal()  # Creating an object of Animal Class
print(cat.breathe())  # Calling a method using object of the Animal Class
print(cat.eat())  # Calling the second method
