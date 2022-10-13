def calculate_age(age):
    return 2022 - int(age)


user_prompt = True

while user_prompt:
    age = input("Please Enter your Age: ")
    if age.isdigit():
        user_prompt = False
    else:
        print("Please enter your age in digits only")

print(f"You were born in {calculate_age(age)}")  # Output: Displays the year user was born
