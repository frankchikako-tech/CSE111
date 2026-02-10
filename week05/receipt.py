"""
Enhancements:
- Prints a reminder of how many days remain until the New Year's Sale (Jan 1).
"""

import csv
from datetime import datetime, date


def read_dictionary(filename, key_column_index):
    """Read a CSV file into a compound dictionary.

    Parameters:
        filename (str): name of the CSV file
        key_column_index (int): column index to use as dictionary key

    Returns:
        dict: dictionary where keys are from key_column_index and
              values are lists containing each row of the CSV
    """
    dictionary = {}

    with open(filename, "r", newline="") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)  # skip header
        for row in reader:
            key = row[key_column_index]
            dictionary[key] = row

    return dictionary


def main():
    try:
        # Read products dictionary
        products_dict = read_dictionary("products.csv", 0)

        print("Inkom Emporium")

        total_items = 0
        subtotal = 0

        # Read customer request file
        with open("request.csv", "r", newline="") as request_file:
            reader = csv.reader(request_file)
            next(reader)  # skip header

            for row in reader:
                product_id = row[0]
                quantity = int(row[1])

                product = products_dict[product_id]
                product_name = product[1]
                price = float(product[2])

                item_total = price * quantity
                subtotal += item_total
                total_items += quantity

                print(f"{product_name}: {quantity} @ {price:.2f}")

        # Calculations
        tax_rate = 0.06
        sales_tax = subtotal * tax_rate
        total = subtotal + sales_tax

        # Output totals
        print(f"Number of Items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {total:.2f}")

        # Thank you message
        print("Thank you for shopping at the Inkom Emporium.")

        # Print current date and time
        current_time = datetime.now()
        print(current_time.strftime("%a %b %d %H:%M:%S %Y"))

        # Enhancement: days until New Year's Sale
        today = date.today()
        next_new_year = date(today.year + 1, 1, 1)
        days_until_new_year = (next_new_year - today).days
        print(f"Days until New Year's Sale: {days_until_new_year}")

    except FileNotFoundError as error:
        print("Error: missing file")
        print(error)

    except PermissionError as error:
        print("Error: permission denied")
        print(error)

    except KeyError as error:
        print("Error: unknown product ID in the request.csv file")
        print(error)


if __name__ == "__main__":
    main()