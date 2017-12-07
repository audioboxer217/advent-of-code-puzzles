''' Look for Infinite Loop in Memory Redistribution '''

def get_largest_block(mem_banks):
    ''' Get the largest memory block and it's index '''

    sorted_banks = sorted(mem_banks, reverse=True)
    largest = sorted_banks[0]
    index = mem_banks.index(largest)

    return index, largest

def redist_blocks(mem_banks, index, blocks):
    ''' Redistribute the memory banks '''

    mem_banks[index] = 0
    index += 1
    mem_bank_size = len(mem_banks)

    for block in range(blocks):
        new_index = index + block
        while new_index >= mem_bank_size:
            new_index -= mem_bank_size
        mem_banks[new_index] += 1

    return mem_banks

def main():
    ''' Look for Infinite Loop in Memory Redistribution '''

    file = open("../puzzle_input.txt")
    mem_banks = [int(x) for x in file.read().split('\t')]
    redistributions = []
    redist_count = 0

    while redistributions.count(str(mem_banks)) <= 1:
        index, largest = get_largest_block(mem_banks)
        mem_banks = redist_blocks(mem_banks, index, largest)
        redistributions.append(str(mem_banks))
        redist_count += 1

    start_of_loop = redistributions.index(str(mem_banks)) + 1
    loop_size = redist_count - start_of_loop

    print("Redistribution Count: %s" % redist_count)
    print("Start of Loop: %s" % start_of_loop)
    print("Loop Size: %s" % loop_size)

if __name__ == '__main__':
    main()
    