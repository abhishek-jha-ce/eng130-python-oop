# Object Oriented Programming

## What is OOP

- Object-oriented programming (`OOP`) is a programming paradigm based on the concept of "`objects`".
- Objects can contain user data and programming code.
- Data are found in the form of fields also known as `attributes` or `properties`.
- Code are used in the form of procedures also known as `methods` or `functions`.

## Four Pillars of OOP

### Abstraction
### Encapsulation
### Inheritance

- Inheritance allows us to define a class that inherits all the methods and properties from another class.

- Parent class is the class being inherited from, also called base class.

- Child class is the class that inherits from another class, also called derived class.


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

