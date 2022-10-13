# Define a method that contains the menu item
def menu_items(category):
    menu_list = {
        "starter": ["Salmon Platter", "Oyesters", "Pappadum", "Empanadilas", "Vol-au-vents", "Dumpling", "Canape"],
        "mains": ["Pasta Bake", "Tteokbokki", "Yakisoba", "Nigri", "Thai Green Curry", "Burger", "Paella", "Pizza"],
        "desserts": ["Cream Brulee", "Mochi", "Apple Pie", "Gulab Jamun", "Dadar Gulung", "Kremes"]
    }
    if category == "starter":
        return menu_list["starter"]
    elif category == "mains":
        return menu_list["mains"]
    elif category == "desserts":
        return menu_list["desserts"]
    else:
        return menu_list


# Define a method that displays the items
def display_items(items):
    for item in range(len(items)):
        print(item+1, ".", items[item])


def take_order(category):
    available_items = menu_items(category)
    display_items(available_items)
    order_item = input(f"Please select a {category}: ")
    if order_item.isdigit():
        return available_items[int(order_item)]
         # order_list.append(available_items[int(order_item)])


order_list = []  # List to hold the order
print("Welcome to \"XYZ\" Restaurant!")
order_list.append(take_order("starter"))
display_items(order_list)

