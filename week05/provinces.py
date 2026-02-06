
def main():
    provinces = []
    with open("provinces.txt", "rt") as file:
        for line in file:
            provinces.append(line.strip())

    print(provinces)

    provinces.pop(0)

    provinces.pop()

    
    for i in range(len(provinces)):
        if provinces[i] == "AB":
            provinces[i] = "Alberta"

   
    alberta_count = provinces.count("Alberta")

   
    print(f"Alberta occurs {alberta_count} times in the modified list.")
if __name__ == "__main__":
    main()