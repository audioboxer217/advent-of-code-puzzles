''' The Halting Problem '''

def add_to_dict(dictionary, item):
    ''' Add an item to the dictionary '''

    item_arr = item.split('\n')
    state = item_arr[0][-2]
    new_value = [item_arr[2][-2], item_arr[6][-2]]
    move = [item_arr[3].split()[-1].replace('.', ''), item_arr[7].split()[-1].replace('.', '')]
    for i, direction in enumerate(move):
        if direction == 'right':
            move[i] = 1
        elif direction == 'left':
            move[i] = -1
        else:
            return False
    new_state = [item_arr[4][-2], item_arr[8][-2]]

    dictionary[state] = {
        '0': {
            'new_value': new_value[0],
            'move': move[0],
            'new_state': new_state[0]
        },
        '1': {
            'new_value': new_value[1],
            'move': move[1],
            'new_state': new_state[1]
        }
    }

    return dictionary

def create_inst_dict(instructions):
    ''' Create a dictionary of the instructions'''

    dictionary = {}

    for inst in instructions:
        dictionary = add_to_dict(dictionary, inst)

    return dictionary

def process_instruction(dictionary, state, turing, index):
    ''' Process the instruction for the current state in the given dictionary '''

    if index >= len(turing):
        turing.append('0')

    instruction = dictionary[state][turing[index]]
    turing[index] = instruction['new_value']
    index += instruction['move']
    state = instruction['new_state']

    if index == -1:
        turing.insert(0, '0')
        index = 0

    return state, turing, index

def main():
    ''' The Halting Problem '''

    instructions = open('../puzzle_input.txt').read().split('\n\n')
    begin = instructions.pop(0).split('\n')
    state = begin[0][-2]
    iterations = int(begin[1].split(' ')[5])

    inst_dict = create_inst_dict(instructions)

    turing = ['0']
    index = 0
    for _ in range(iterations):
        state, turing, index = process_instruction(inst_dict, state, turing, index)

    checksum = turing.count('1')
    print(checksum)

if __name__ == '__main__':
    main()
    