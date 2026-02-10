import csv
from datetime import datetime

dictionary = {}

def read_dictionary(filename, key_column_index):
    with open(filename, "r") as csv_file:
        csvreader = csv.reader(csv_file, delimiter=",")
        next(csvreader) 
        for row in csvreader:
            key_value = row[key_column_index]
            dictionary[key_value] = row
        return dictionary
    
def main():
    try:
        subtotal = 0.0
        total = 0.0
        KEY_INDEX = 0
        NAME_INDEX = 1
        PRICE_INDEX = 2
        product_dict = read_dictionary("products.csv", KEY_INDEX)
        print(product_dict)
        with open("request.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)  
            for row in reader:
                product_id = row[0]
                quantity = int(row[1])
                product = product_dict[product_id]
                name = product[NAME_INDEX]
                price = float(product[PRICE_INDEX])
                print(f"Product name: {name}, Price: ${price}")
                item_total = price * quantity
                subtotal += item_total
                total += item_total
                total_items = total_items + quantity if 'total_items' in locals() else quantity
                print(f"{name}: {quantity} @ ${price} ")
        
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
        today = datetime.today()
        next_new_year = datetime(today.year + 1, 1, 1)
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