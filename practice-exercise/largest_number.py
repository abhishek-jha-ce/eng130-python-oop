# To find the largest number in the list
# Sort the List
# Return the Last number in the list - It will always be the largest in the sorted list

def find_largest(numbers):
    numbers.sort()
    return numbers[-1]


num = [3, 7, 8, 101, 12, 15, 3, 2]
print(f"The largest number in the list: {find_largest(num)}")
def find_largest(numbers):
    numbers.sort()  # Sorting the list
    return numbers[-1]  # The largest number will always be the last one


num = [3, 7, 19, 5, 114, 12, 54, 1]
print(f"The largest number in the list: {find_largest(num)}")
