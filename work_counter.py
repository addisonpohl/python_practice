from datetime import datetime

# Basic stuture for a productivity counter
# Todo:
# Add ability to remove from counter
# Allow option to switch time to 12 hour format
# Add tkinter for gui. Buttons should replace entering 1 to update counter
# Maybe use a class convert to class? Depends on how many objects will be added to

counter = 0
start = datetime.time(datetime.now())
print(f"Start time: {start}")
while True:

    count = input("> ")

    try:
        if int(count) == 1:
            counter += 1
        else:
            print("Enter '1' to increase count")

    except ValueError:
        if count.lower() == "total":
            print(counter)
        elif count.lower() == "exit":
            print(counter)
            break
