''' Coprocessor Conflagration '''

REGISTER = {"a": 0, "b": 0, "c": 0, "d": 0, "e": 0, "f": 0, "g": 0, "h": 0}

def get_value(item):
    ''' Checks if 'item' is an int or a reference and returns accordingly. '''

    try:
        int(item)
    except ValueError:
        return REGISTER[item]

    return int(item)

def main():
    ''' Coprocessor Conflagration '''

    instructions = open('../puzzle_input.txt').read().split('\n')
    inst_length = len(instructions)

    i = 0
    count = 0
    while i < inst_length and i >= 0:
        ins = instructions[i].split(' ')
        print('instruction %s: %s' % (i, ins))
        if ins[0] == 'set':
            REGISTER[ins[1]] = get_value(ins[2])
            i += 1
        elif ins[0] == 'sub':
            REGISTER[ins[1]] = get_value(ins[1]) - get_value(ins[2])
            i += 1
        elif ins[0] == 'mul':
            REGISTER[ins[1]] = get_value(ins[1]) * get_value(ins[2])
            count += 1
            i += 1
        elif ins[0] == 'jnz':
            if get_value(ins[1]) != 0:
                i += get_value(ins[2])
            else:
                i += 1

    print(count)

if __name__ == '__main__':
    main()
    