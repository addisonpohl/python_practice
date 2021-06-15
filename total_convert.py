# This script is meant to take prices, total them, and convert to USD.
import sys
from currency_converter import CurrencyConverter
c = CurrencyConverter()
print("Enter Values Followed By a Currency. Example: 10 499.99 EUR:\n")


while True:
    # loops user input until specified
    values = input("> ")
    if values.lower() == "stop" or values.lower() == "exit":
        sys.exit()
    else:
        currency = values[-3:].upper()
        values = values[:-4]
        total_list = values.split(" ")

        for index, item in enumerate(total_list):
            # checks datatype to determine needed conversion
            if "." in item:
                total_list[index] = float(item)
            else:
                total_list[index] = int(item)

        sum_total = sum(total_list)

        try:
            # verifies if the proper format was entered
            converted = round(c.convert(sum_total, currency, "USD"), 2)
        except ValueError:
            print("Please use this format - Ex: 199.15 10.99 13 EUR")
        else:
            print(f'Complete: {converted}')
