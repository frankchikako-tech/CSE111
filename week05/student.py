import csv



dict = {}


def read_dictionary(filename, key_column_index):
    with open(filename, "r") as csv_file:
        csvreader = csv.reader(csv_file, delimiter=",")
        
        for row in csv_file:
            key_value = row[key_column_index]
            dict[key_value] = row
        return dict
            
def main():
   KEY_INDEX = 0
   NAME_INDEX = 1
   students = read_dictionary("students.csv", KEY_INDEX)
   print(students)


if __name__=="__main__":
    main()

