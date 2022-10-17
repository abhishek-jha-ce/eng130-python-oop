# this function returns the sum of even number
def even_number(num):
    even_total = 0
    for i in range(1, num + 1):  # To print from 1 to num in argument
        print(i)
        if i % 2 == 0:
            even_total += i

    return even_total


# This function counts how many odd numbers in the range
def odd_number(num):
    odd_counter = 0

    for i in range(1, num + 1):
        if i % 2 != 0:
            odd_counter += 1

    return odd_counter


print("Sum of Even Numbers: " + str(even_number(100)))
print("Total of Odd Numbers: " + str(odd_number(100)))
