# function to find the largest number
def find_largest(numbers):
    numbers.sort()  # Sorting the list
    return numbers[-1]  # The largest number will always be the last one


num = [3, 7, 19, 5, 114, 12, 54, 1]
print(f"The largest number in the list: {find_largest(num)}")
