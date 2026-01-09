#Assignment: Tire Volume Calculator with Logging
#This program calculates the volume of a tire based on user input and logs the results to a file.
# Student name : Ukeje Frank Chika


import math 
from datetime import datetime
date = datetime.now().date()

with open("tire_volumes.txt", "a") as file:
    print(f"Tire Volume Calculations - {date}", file=file)
    width = float(input("Enter the width of the tire in mm: "))
    aspect_ratio = float(input("Enter the aspect ratio of the tire: "))
    diameter = float(input("Enter the diameter of the wheel in inches: "))
    volume = (math.pi * width**2 * aspect_ratio * (width * aspect_ratio + 2540 * diameter)
            ) / 10000000000
    print(f"The approximate volume is {volume:.2f} liters")
    buy = input("Do you want to buy the tire with the dimension entered? (yes/no): ").strip().lower()
    if buy == 'yes':
        phone = input("Enter your phone number: ")
        print("Thank you for your purchase! We will contact you soon.")
    else:
        print("No worries! Feel free to explore other options.")    

    print(f"{date}, {width}, {aspect_ratio}, {diameter}, {volume:.2f}, {phone}", file=file)
    #print(f"Aspect Ratio: {aspect_ratio}", file=file)
    #print(f"Diameter: {diameter} inches", file=file)
    #print(f"Volume: {volume:.2f} liters", file=file)

