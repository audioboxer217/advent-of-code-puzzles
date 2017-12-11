''' Knot Hash '''

def update_list_with_sublist(input_list, sublist, begin, end):
    ''' Updates a given list with a sublist starting at 'begin' and going to 'end'  '''

    list_size = len(input_list)
    sub_idx = 0
    for idx in range(begin, end):
        if idx >= list_size:
            idx -= list_size
        input_list[idx] = sublist[sub_idx]
        sub_idx += 1

    return input_list

def main():
    ''' Knot Hash '''

    input_list = list(range(0, 256))
    file = open("../puzzle_input.txt")
    hash_lengths = map(int, file.read().split(","))
    input_size = len(input_list)

    index = 0
    skip_size = 0
    for length in hash_lengths:
        capture = index + length
        if capture >= input_size:
            capture -= input_size
            sublist1 = input_list[index:input_size]
            sublist2 = input_list[:capture]
            sublist = sublist1 + sublist2
        else:
            sublist = input_list[index:capture]
        sublist.reverse()
        input_list = update_list_with_sublist(input_list, sublist, index, index + length)
        movement = capture + skip_size
        if movement >= input_size:
            movement -= input_size
        index = movement
        skip_size += 1

    answer = input_list[0] * input_list[1]
    print("Answer: %s" % answer)

if __name__ == '__main__':
    main()
    