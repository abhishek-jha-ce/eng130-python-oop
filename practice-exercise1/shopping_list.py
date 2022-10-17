def print_values(shop_item):
    for item in shop_item:
        print(item)


def print_items_with_cost(shop_item):
    for item, value in shop_item.items():
        print(item + " - " + str(value))


def print_total(shop_item):
    total = 0
    for value in shop_item.values():
        total += value

    return total


shopping_items = {
    "eggs": 1.85,
    "bread": 1.50,
    "peppers": 0.90
}

# Print only values
print_values(shopping_items)

# Print items with it's cost
print_items_with_cost(shopping_items)
print("The total is: " + str(print_total(shopping_items)))
