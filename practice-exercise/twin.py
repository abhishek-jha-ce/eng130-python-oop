# Pseudo Code
# Get the two strings
# Change the number to lowercase - to make sure it's case in-sensitive
# Sort the number - using the sorted method
# Return the value - either True if they contain the same character or False


def is_twin(a, b):
    return sorted(a.lower()) == sorted(b.lower())


str1 = "Silent"
str2 = "Listen"
print(f"The Number are twin?: {is_twin(str1, str2)}")  # Calling the function
