''' Disk Defragmentation - Part 1 '''

HASH_LENGTH_SUFFIX = [17, 31, 73, 47, 23]
LIST_SIZE = 256

def get_sublist(sparse_hash, index, length):
    ''' Get the sublist from the main list '''

    sublist = []
    for sub_idx in range(length):
        sublist.append(sparse_hash[(sub_idx+index) % LIST_SIZE])

    sublist.reverse()

    return sublist

def update_list_with_sublist(sparse_hash, sublist, index, length):
    ''' Updates a given list with a sublist starting at 'begin' and going to 'end'  '''

    for idx in range(length):
        sparse_hash[(idx + index) % LIST_SIZE] = sublist[idx]

    return sparse_hash

def calculate_sparse_hash(sparse_hash, hash_lengths, index, skip_size):
    ''' Calculates the Knot Hash '''

    for length in hash_lengths:
        sublist = get_sublist(sparse_hash, index, length)
        sparse_hash = update_list_with_sublist(sparse_hash, sublist, index, length)
        # index += length + skip_size
        index += length + skip_size
        skip_size += 1

    return sparse_hash, index, skip_size

def calculate_dense_hash(sparse_hash):
    ''' Calculates the Dense Hash from the given knot_hash '''

    hash_list = list(range(16))
    for itr in range(16):
        hash_list[itr] = sparse_hash[(16*itr)]^sparse_hash[(16*itr)+1]^sparse_hash[(16*itr)+2]^sparse_hash[(16*itr)+3]^sparse_hash[(16*itr)+4]^sparse_hash[(16*itr)+5]^sparse_hash[(16*itr)+6]^sparse_hash[(16*itr)+7]^sparse_hash[(16*itr)+8]^sparse_hash[(16*itr)+9]^sparse_hash[(16*itr)+10]^sparse_hash[(16*itr)+11]^sparse_hash[(16*itr)+12]^sparse_hash[(16*itr)+13]^sparse_hash[(16*itr)+14]^sparse_hash[(16*itr)+15]

    for idx, item in enumerate(hash_list):
        hex_val = hex(item).replace("0x", "")
        if len(hex_val) == 1:
            hex_val = "0" + hex_val
        hash_list[idx] = hex_val
    dense_hash = "".join(hash_list)

    return dense_hash

def get_knot_hash(hash_input):
    ''' Get the Knot Hash for the row '''
    hash_lengths = []
    sparse_hash = list(range(256))
    index = 0
    skip_size = 0
    for char in hash_input:
        hash_lengths.append(ord(char))
    hash_lengths.extend(HASH_LENGTH_SUFFIX)

    for i in range(64):
        sparse_hash, index, skip_size = calculate_sparse_hash(sparse_hash,
                                                              hash_lengths,
                                                              index,
                                                              skip_size)


    dense_hash = calculate_dense_hash(sparse_hash)

    return dense_hash

def main():
    ''' Disk Defragmentation '''

    knot_hash = open('../puzzle_input.txt').read()

    grid = []
    for i in range(128):
        row = get_knot_hash(knot_hash + '-' + str(i))
        binary = (bin(int(row, 16))[2:])
        grid.append(list((128-len(binary)) * "0" +  binary))

    count = 0
    for row in grid:
        used = row.count('1')
        count += used

    print(count)

if __name__ == '__main__':
    main()
    