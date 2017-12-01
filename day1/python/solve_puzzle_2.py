"""Simple addition of numbers in a list when two numbers match halfway through the list"""

def add_numbers_by_criteria(num_list, key_match):
    """Iterate through file and add the numbers together
    when two numbers match halfway through the list"""

    total = 0
    for index, curr_num in enumerate(num_list):
        if index < key_match:
            halfway = index + key_match
        else:
            halfway = index - key_match

        halfway_num = num_list[halfway]

        if curr_num == halfway_num:
            total += int(curr_num)

    return total

def main():
    """Run add_numbers_by_criteria"""

    file = open("../puzzle_input.txt")
    num_list = list(file.read())
    key_match = int(len(num_list)/2)

    total = add_numbers_by_criteria(num_list, key_match)

    print(total)

if __name__ == '__main__':
    main()
    