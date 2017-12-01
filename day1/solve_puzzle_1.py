"""Simple addition of numbers in a list when there are two consecutive nubmers"""

def add_numbers_from_file(file, number):
    """Iterate through file and add the numbers together when there are two consecutive numbers"""

    last_num = number
    total = 0
    with file:
        while True:
            curr_num = file.read(1)

            if curr_num:
                if curr_num == last_num:
                    total += int(curr_num)
                last_num = curr_num
            else:
                return total, last_num

def main():
    """Run add_numbers_from_file"""
    file = open("puzzle_input.txt")

    first_num = file.read(1)

    total, last_num = add_numbers_from_file(file, first_num)

    if first_num == last_num:
        total += int(first_num)

    print(total)

if __name__ == '__main__':
    main()
    