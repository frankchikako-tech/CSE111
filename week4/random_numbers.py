import random


def append_random_number(number_list, quantity=1):

    for _ in range(quantity):
        random_number = random.uniform(0, 100)
        rounded = round(random_number, 1)
        number_list.append(rounded)
    

def append_random_word(word_list, quantity=1):
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]

    for _ in range(quantity):
        random_word = random.choice(words)
        word_list.append(random_word)






def main():
    number_list = [16.2, 75.1, 52.3]
    print(f"The number_list: {number_list}")

    append_random_number(number_list)

    print(f"The number List: {number_list}")


    append_random_number(number_list, 3)

    print(f"The number List: {number_list}")

    word_list = []
    append_random_word(word_list, 5)
    print(f"The word_list: {word_list}")







if __name__ == "__main__":
    main()







