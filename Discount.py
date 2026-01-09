# Student name : Ukeje Frank Chika
# assignment on discount
from datetime import datetime
discount_rate = 0.1
sale_tax_rate = 0.06
weekday = datetime.now().weekday()

# get the quantity and price of each items
# Prompt the user for a subtotal
print("Enter the quantity and price of each item")
subtotal =0
quantity = 99
while quantity != 0:
    quantity = int(input("Enter the quantity of the item "))
    if quantity != 0:
        price = float(input("Enter the price of the item "))
        subtotal += quantity*price       
print(f"Subtotal: ${subtotal:.2f}")
# Determine if a discount is applicable
if weekday == 1 or weekday == 2:
    if subtotal >= 50:
        discounts = subtotal*discount_rate
        subtotal = subtotal-discounts
        print(f"The discount: ${discounts:.2f}")
    else:
        print(f"You need to purchase ${50 - subtotal:.2f} more to qualify for the discount.")        
else:
    print("If you come on Tuesday or Wednesday, a discount of 10% will be applied")
    
sales_tax = subtotal*sale_tax_rate
total_due = subtotal+sales_tax
print(f"Sales tax amount: ${sales_tax:.2f}")
print(f"Total due: ${total_due:.2f}")       