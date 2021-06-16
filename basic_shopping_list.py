# future ideas:
# Add ability to export list to a document
# Add a gui and link functions to buttons


shopping_list = []


def show_help():
    """displays a the list of commands"""
    print("What should we pickup at the store?")
    print("""
    Enter 'SHOW' to display current list.
    Enter 'DONE' to stop adding items.
    Enter 'REMOVE' followed by name to remove an item. Ex: REMOVE Orange
    Enter 'HELP' if you would like to reference the commands.
    """)


def add_to_list(item):
    # adds items to the shopping list
    shopping_list.append(item.title())
    if len(shopping_list) == 1:
        print("Added! List has 1 item.")
    else:
        print(f"Added! List has {len(shopping_list)} items.")


def rm_from_list(item):
    # removes mentioned item from list
    item = item[7:].title()
    if item in shopping_list:
        shopping_list.remove(item)
    else:
        print("This item was not found in your list.")


def show_list():
    # displays the shopping list for the user
    print("\n    Shopping List   \n")
    for index, item in enumerate(shopping_list, start=1):
        print(f"{str(index)}. {item}")
    print()


while True:
    # Loops the user input until the user states they are done
    new_item = input("> ")
    if new_item.upper() == "DONE":
        break
    elif new_item.upper() == "HELP":
        show_help()
    elif new_item.upper() == "SHOW":
        show_list()
    elif "REMOVE" in new_item.upper():
        rm_from_list(new_item)
        show_list()
    else:
        add_to_list(new_item)

show_list()
