# Object Oriented Programming

## What is OOP

- Object-oriented programming (`OOP`) is a programming paradigm based on the concept of "`objects`".
- Objects can contain user data and programming code.
- Data are found in the form of fields also known as `attributes` or `properties`.
- Code are used in the form of procedures also known as `methods` or `functions`.

## Four Pillars of OOP

### Abstraction

- It is a process of handling complexity by hiding unnecessary information from the user.
- It lets user to implement complex logic on top, without understanding about all the hidden background/back-end complexity.
- We can achieve abstraction by using abstract classes and methods in our programs.
- Abstraction can be either `data abstraction` or `process abstraction`.

<p align="center">
  <img src="https://user-images.githubusercontent.com/110366380/195639042-e807bb9a-11b8-4807-9ec0-e4cc21851f14.png">
</p>

#### Example:

```commandline
import math

number = 2.34

print(math.ceil(number))   # Output: 3
print(math.floor(number))  # Output: 2
```

In this example we round the number as required, but we don't have to write the code that does the work. 
This is an example of abstraction.

### Encapsulation

- Encapsulation is the concept of bundling data and methods within a single Unit.
- A class can be an example of encapsulation as it binds all the data members (variables) and methods into a single unit.
- It provides well-defined, readable code.
- Encapsulation is useful in putting the restrictions on accessing variables and methods directly thus preventing accidental modification of data.

<p align="center">
  <img src="https://user-images.githubusercontent.com/110366380/195642103-ba26c602-73f3-416f-9d8b-ad31921b1979.png">
</p>

#### Example:

```commandline
class Counter:
    def __init__(self):
        self.current = 0  # Initial value when an instance is created

    def increment(self):  # Method increases the value of the current attribute by 1.
        self.current += 1

    def value(self):      # Method to return the current value of the attribute.
        return self.current

    def reset(self):      # Method to reset/set the current value to 0.
        self.current = 0



counter = Counter()  # Creates a new instance of Counter class - Counter initialize to 0


counter.increment()  # Counter Value: 1
counter.increment()  # Counter Value: 2
counter.increment()  # Counter Value: 3

print(counter.value())  # Output: 3
```

### Inheritance

- Inheritance refers to defining a new class with little or no modificatin to an existing class.
- It allows us to define a class that inherits all the methods and properties from another class.
- Parent class is the class being inherited from, also called base class.
- Child class is the class that inherits from another class, also called derived class.

<p align="center">
  <img src="https://user-images.githubusercontent.com/110366380/195652077-3c604f16-2dba-4353-901f-c0915e6db293.png">
</p>

#### Example: parent class/base class [person.py]
```
# A program to demonstrate inheritance

class Person(object):

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
    
    def display(self):
        print(self.name, self.id)


emp = Person("Abhishek", 101)  # Creating a new instance of Person
emp.display()  # Output Abhishek 101
```
#### Example: child class/ derived class [employee.py]
```
from person import Person  # Don't forget to import the class else it won't work


class Emp(Person):  # The parent class within the brackets

    def child_function(self):
        print("This function can only be called by this class")


Emp_details = Emp("Ayush", 102)  # Creating a new instance of Person

Emp_details.display()  # Calling parent class function

Emp_details.child_function()  # Calling child class function

Output:
Abhishek 101
Ayush 102
This function can only be called by this class
```

### Polymorphism

- Polymorphism means multiple forms, same operator or function can take multiple forms. 
- It is also useful in creating different classes which will have class methods with same name.
- It helps in re-using a lot of code and decreases code complexity. 
- Polymorphism is also linked to inheritance.

#### Example

The '`+`' Operator. It adds two numbers if they are integers, but concatenates if they are string.

```commandline
a = 23
b = 11

s1 = "Hello"
s2 = "There!"

print(a+b)  # Output: 34
print(s1+s2)  # Output: HelloThere!
```


