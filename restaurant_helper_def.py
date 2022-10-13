# Define a method that contains the menu item and returns
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
def display_items(items, category):
    print(f"\n ***** {category.capitalize()} list *****")  # For formatting purpose only
    for item in range(len(items)):
        print(item+1, ".", items[item])  # Prints all the items that is in the list


# Define a method that takes the order
def take_order(category):
    available_items = menu_items(category)  # Get the available items from the menu items
    display_items(available_items, category)  # Displays all the available items
    order_item = input(f"Please select Your {category.capitalize()}: ")  # Customer selects what they want
    if order_item.isdigit():
        return available_items[int(order_item)-1]  # the selected item is returned to be appended to order list


order_list = []  # List to hold the order
print("Welcome to \"XYZ\" Restaurant!")
order_list.append(take_order("starter"))     # Starter Order
order_list.append(take_order("mains"))       # Mains Order
order_list.append(take_order("desserts"))    # Desserts Order
display_items(order_list, "customer order")  # Displays the Customer Order
