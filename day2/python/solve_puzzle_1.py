"""Calculates a Checksum from CSV"""

import csv

def get_values(row):
    """Gets the largest and smallest values from a list of numbers"""
    smallest = row[0]
    largest = row[0]
    for curr_num in row:
        if int(curr_num) < int(smallest):
            smallest = curr_num
        if int(curr_num) > int(largest):
            largest = curr_num
    return smallest, largest

def main():
    """Calculates a Checksum from CSV"""
    with open("../puzzle_input.csv") as file:
        csv_reader = csv.reader(file, delimiter='\t')
        num_list = []
        for row in csv_reader:
            smallest, largest = get_values(row)
            difference = int(largest) - int(smallest)
            num_list.append(int(difference))
        checksum = sum(num_list)
        print("Checksum: %s" % checksum)

if __name__ == '__main__':
    main()
    