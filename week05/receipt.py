import csv


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
            print(f"{product_name}: {quantity} @ ${price} ")

if __name__ == "__main__":
    main()