# Program to check for what movies a user can watch

def rating(age):
    if age > 18:  # If adult, you can watch any movies.
        print("You are " + user_age + " year Old. You can watch any movies you like")
    elif age > 15:  # If Older than 15
        print("You are " + user_age + " year Old. You can only watch \"U\" , \"PG\", \"12\" and, \"15\" rated movies")
    elif age > 12:
        print("You are " + user_age + " year Old. You can only watch \"U\" , \"PG\" and, \"12\" rated movies")
    elif age > 8:
        print("You are " + user_age + " year Old. You can only watch \"U\" and \"PG\" rated movies")
    else:
        print("You are " + user_age + " year Old. You can only watch \"U\" rated movies")


user_prompt = True

while user_prompt:
    user_age = input("Please enter your age: ")  # Ask User for their age
    if user_age.isdigit():  # Checks if the user has input numbers only
        if int(user_age) < 117:  # Checks if the user is less than 117 years old
            user_prompt = False
        else:
            print("You must be less than 117 Years Old!")
    else:
        print("Please enter a valid number")

# Calling the function which determines the rating of the user
rating(int(user_age))
