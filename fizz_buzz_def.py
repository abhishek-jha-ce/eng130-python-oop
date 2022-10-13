# Define a method to print Fizz
def fizz():
    print("Fizz")


# Define a method to print Buzz
def buzz():
    print("Buzz")


# Define a method to print FizzBuzz
def fizzbuzz():
    print("FizzBuzz")


# Ask user to choose the number for Fizz
fizz_number = int(input("On which number's multiple do you want to print \"Fizz\": "))

# Ask user to choose the number for Buzz
buzz_number = int(input("On which number's multiple do you want to print \"Buzz\": "))

# Loop the given range 1 to 100 and print the matching word if condition met else print the number itself
for num in range(1, 101):
    if num % fizz_number == 0 and num % buzz_number == 0:
        fizzbuzz()
    elif num % fizz_number == 0:
        fizz()
    elif num % buzz_number == 0:
        buzz()
    else:
        print(num)
