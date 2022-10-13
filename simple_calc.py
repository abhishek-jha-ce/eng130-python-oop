def add(num1, num2):
    return num1 + num2


def sub(num1, num2):
    return num1 - num2


def mul(num1, num2):
    return num1 * num2


def div(num1, num2):
    return num1 / num2


print("Select The Calculation Required.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

user_prompt = True

while user_prompt:
    # Ask the user for their choice of calculation
    choice = input("Select your choice: ")

    if choice in ('1', '2', '3', '4'):
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))

        elif choice == '2':
            print(num1, "-", num2, "=", sub(num1, num2))

        elif choice == '3':
            print(num1, "*", num2, "=", mul(num1, num2))

        elif choice == '4':
            print(num1, "/", num2, "=", div(num1, num2))

        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Do you want more calculation? (yes/no): ")
        if next_calculation == "no":
            break

    else:
        print("Invalid Input")
