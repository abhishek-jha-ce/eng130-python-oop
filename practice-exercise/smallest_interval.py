# Find the smallest interval between two numbers in the list
# sort the number first
# return the difference between the second and first number in the list


def find_smallest_interval(num):
    num.sort()
    return num[1] - num[0]


numbers = [12, 3, 4, 89, 23, 7]
print(find_smallest_interval(numbers))
