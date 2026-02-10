import csv



dict = {}


def read_dictionary(filename, key_column_index):
    with open(filename, "r") as csv_file:
        csvreader = csv.reader(csv_file, delimiter=",")
        next(csvreader)  # Skip the header row
        
        for row in csvreader:

            key_value = row[key_column_index]
            dict[key_value] = row
        return dict
            
def main():
   KEY_INDEX = 0
   NAME_INDEX = 1
   students = read_dictionary("students.csv", KEY_INDEX)
   inumber = input("Enter the student's number: ")
   inumber = inumber.replace("- ", "")
   if not inumber.isdigit():
       print("Invalid input. Please enter a valid student number.")
   else:
       
       if inumber in students:
           student = students[inumber]
           name = student[NAME_INDEX]
           print(f"Student name: {name}")
       elif len(inumber) != 9:
           print("An inumber must be 9 digits long.")
       elif len(inumber) == 9 and inumber.isdigit() and inumber not in students:
           print("No such student.")

       else:
              print("No such student.")
       
  # student = students[inumber]
   #name = student[NAME_INDEX]
   #if inumber not in students:
    #   print("No such student.")
   #else:
    #    print(f"Student name: {name}")


if __name__=="__main__":
    main()

