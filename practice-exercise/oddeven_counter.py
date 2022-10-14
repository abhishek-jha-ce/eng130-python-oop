# Odd Even Counter
# Define a list that contains two numbers, initialized to 0
# The argument we received we check if it is even or odd
# If it is even we add the value to the 1st variable in list
# If it is odd we add it to the second variable in list
# Decrement the number by 1 and follow the same till the number is 0

def odd_even_counter(number):
    counter_list = [0, 0]
    while number != 0:
        if number % 2 == 0:
            counter_list[0] += number
        else:
            counter_list[1] += number

        number -= 1

    return counter_list


num = 5
print(odd_even_counter(num))
