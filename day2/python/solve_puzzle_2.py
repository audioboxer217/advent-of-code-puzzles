"""Calculates a Checksum from CSV"""

import csv

def get_values(row):
    """Gets the largest and smallest values from a list of numbers"""
    for curr_num in row:
        for num in row:
            if num != curr_num:
                mod_check = int(curr_num)%int(num)
                if mod_check == 0:
                    value = int(curr_num)/int(num)
                    return value

def main():
    """Calculates a Checksum from CSV"""
    with open("../puzzle_input.csv") as file:
        csv_reader = csv.reader(file, delimiter='\t')
        num_list = []
        for row in csv_reader:
            value = get_values(row)
            num_list.append(int(value))
        checksum = sum(num_list)
        print("Checksum: %s" % checksum)

if __name__ == '__main__':
    main()
    