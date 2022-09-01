import sys
import csv
import regex
import pickle

# Used in error checking for middle initial. Incase initial is a single digit or other character
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

# Person class, used to populate dictionary. Saved and read via pickle
class Person:
    def __init__(self, last_name : str, first_name : str, middle_initial : str, id : str, phone : str):
        self.last_name = last_name
        self.first_name = first_name
        self.middle_initial = middle_initial
        self.id = id
        self.phone = phone

    def display(self):
        print(f'Employee id: {self.id}')
        print(f'\t\t{self.first_name} {self.middle_initial} {self.last_name}')
        print(f'\t\t{self.phone}')


def read_input_file_and_process_data():
    person_dictionary = dict()
    with open(str(sys.argv[1])) as csvfile:
        lines = csv.reader(csvfile)
        for i, row in enumerate(lines):
            if i > 0:
                # Capitalize last name
                row[0] = row[0].capitalize()

                # Capitalize first name
                row[1] = row[1].capitalize()

                # Automatic error checking for middle initial
                if len(row[2]) != 1 or row[2] not in alphabet:
                    row[2] = 'X'
                row[2] = row[2].capitalize()

                # Error checking for valid ID
                while not regex.match('^[A-Z]{2}[0-9]{4}$', row[3]):
                    print(f'{row[3]} is an invalid employee id for {row[1]} {row[0]}.\nID is two capital letters followed by 4 digits')
                    row[3] = input('Please enter a valid id: ')

                # Error checking for valid phone number
                while not regex.match('^[0-9]{3}-[0-9]{3}-[0-9]{4}$', row[4]):
                    print(f'{row[4]} is an invalid phone number format for {row[1]} {row[0]}.\nPhone numbers are in the format 123-456-7890')
                    row[4] = input('Please enter a valid phone number: ')

                # Creating person object
                current_person = Person(row[0], row[1], row[2], row[3], row[4])

                # Checking for duplicate ids in dictionary
                if current_person.id in person_dictionary:
                    print(f'{current_person.id} is already an existing ID! Skipping {current_person.first_name}'
                          f' {current_person.last_name}')
                else:
                    person_dictionary[current_person.id] = current_person

    return person_dictionary

if __name__ == "__main__":
    # Error checking for file path to data in sysarg
    if len(sys.argv) < 2:
        print('File location for data csv not given in sysarg. Program ending')
    else:
        person_dictionary = read_input_file_and_process_data()
        # Saving the dictionary in binary to dict.p
        pickle.dump(person_dictionary, open('dict.p', 'wb'))

        # Reading in the dict.p and printing the contents of dictionary
        dict_in = pickle.load(open('dict.p', 'rb'))

        # Added print statement for formatting
        print()
        print(f'Employee list:\n')
        for person in dict_in.values():
            person.display()
            print()
