# Menu dictionary
menu = {
    "Snacks": {
        "Cookie": .99,
        "Banana": .69,
        "Apple": .49,
        "Granola bar": 1.99
    },
    "Meals": {
        "Burrito": 4.49,
        "Teriyaki Chicken": 9.99,
        "Sushi": 7.49,
        "Pad Thai": 6.99,
        "Pizza": {
            "Cheese": 8.99,
            "Pepperoni": 10.99,
            "Vegetarian": 9.99
        },
        "Burger": {
            "Chicken": 7.49,
            "Beef": 8.49
        }
    },
    "Drinks": {
        "Soda": {
            "Small": 1.99,
            "Medium": 2.49,
            "Large": 2.99
        },
        "Tea": {
            "Green": 2.49,
            "Thai iced": 3.99,
            "Irish breakfast": 2.49
        },
        "Coffee": {
            "Espresso": 2.99,
            "Flat white": 2.99,
            "Iced": 3.49
        }
    },
    "Dessert": {
        "Chocolate lava cake": 10.99,
        "Cheesecake": {
            "New York": 4.99,
            "Strawberry": 6.49
        },
        "Australian Pavlova": 9.99,
        "Rice pudding": 4.99,
        "Fried banana": 4.49
    }
}

# 1. Set up order list. Order list will store a list of dictionaries for
# menu item name, item price, and quantity ordered
order_list = []


# Launch the store and present a greeting to the customer
print("Welcome to the variety food truck.")

# Customers may want to order multiple items, so let's create a continuous
# loop
place_order = True
while place_order:
    # Ask the customer from which menu category they want to order
    print("From which menu would you like to order? ")

    # Create a variable for the menu item number
    i = 1
    # Create a dictionary to store the menu for later retrieval
    menu_items = {}

    # Print the options to choose from menu headings (all the first level
    # dictionary items in menu).
    for key in menu.keys():
        print(f"{i}: {key}")
        # Store the menu category associated with its menu item number
        menu_items[i] = key
        # Add 1 to the menu item number
        i += 1

    # Get the customer's input
    menu_selection = input("Type menu number: ")

    # Check if the customer's input is a number
    if menu_selection.isdigit():
        # Check if the customer's input is a valid option
        if int(menu_selection) in menu_items.keys():
            # Save the menu category name to a variable
            menu_selection_name = menu_items[int(menu_selection)]
            # Print out the menu category name they selected
            print(f"You selected {menu_selection_name}")

            # Print out the menu options from the menu_selection_name
            print(f"What {menu_selection_name} item would you like to order?")
            i = 1
            menu_items = {}
            print("Item # | Item name                | Price")
            print("-------|--------------------------|-------")
            for key, value in menu[menu_selection_name].items():
                # Check if the menu item is a dictionary to handle differently
                if type(value) is dict:
                    for key2, value2 in value.items():
                        num_item_spaces = 24 - len(key + key2) - 3
                        item_spaces = " " * num_item_spaces
                        print(f"{i}      | {key} - {key2}{item_spaces} | ${value2}")
                        menu_items[i] = {
                            "Item name": key + " - " + key2,
                            "Price": value2
                        }
                        i += 1
                else:
                    num_item_spaces = 24 - len(key)
                    item_spaces = " " * num_item_spaces
                    print(f"{i}      | {key}{item_spaces} | ${value}")
                    menu_items[i] = {
                        "Item name": key,
                        "Price": value
                    }
                    i += 1
            # 2. Ask customer to input menu item numbern
            
            menu_item = input("Type item number: ")



            # 3. Check if the customer typed a number
            if menu_item.isdigit():
                # Convert the menu selection to an integer
                menu_item_number = int(menu_item)
            


                # 4. Check if the menu selection is in the menu items
                if menu_item_number in menu_items.keys():
                        selected_item = menu_items[menu_item_number]
                        quantity = input(f"How many {selected_item['Item name']} would you like?")
                        if not quantity.isdigit():
                            quantity = 1
                        else:
                            quantity = int(quantity)
                        order_list.append({
                            "Item name": selected_item["Item name"],
                            "Price": selected_item["Price"],
                            "Quantity": quantity
                        })
                else:
                    print(f"Item #{menu_item_number} is not available." )
            else:
                print("You didn't enter a valid menu number.")
                    


                    

        else:
            # Tell the customer they didn't select a menu option
            print(f"{menu_selection} was not a menu option.")
    else:
        # Tell the customer they didn't select a number
        print("You didn't select a number.")

    while True:
        keep_ordering = input("Would you like to keep ordering? (Y)es or (N)o ").upper()
        match keep_ordering:
            case 'Y':
                break  # Exit the inner loop if 'Y' is selected
            case 'N':
                place_order = False
                break  # Exit the outer loop and inner loop if 'N' is selected
            case _:
                print("Please enter 'Y' for yes or 'N' for no.")

# Thank the customer and potentially display the order (optional)
print("Thank you for your order!")
       
print("This is what we are preparing for you.\n")



print("Item name                 | Price  | Quantity")
print("-" *26 + "|" + "-" *8 + "|" + "-" *11)

total_price = 0
for item in order_list:
    item_name = item["Item name"]
    item_price = item["Price"]
    item_quantity = item["Quantity"]

    
    formatted_price = f"${item_price:.2f}"
    print(f"{item_quantity}x {item_name:<30} {formatted_price:>8}")  # Align right, pad left

    total_price += item_price * item_quantity

total_cost = sum(item["Price"] * item["Quantity"] for item in order_list)
print(f"\nTotal cost : ${total_cost:.2f}")
print ("Thanks for dining with us!")




