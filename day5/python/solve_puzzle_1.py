''' Follow instructions to exit maze '''

def jump(index, instructions):
    ''' Jumps from the current index the one given in the index's value '''

    try:
        next_index = index + int(instructions[index])
        new_value = int(instructions[index]) + 1
        instructions[index] = new_value
    except IndexError:
        next_index = 'escaped'
    return next_index

def main():
    ''' Follow instructions to exit maze '''

    file = open("../puzzle_input.txt")
    instructions = file.read().split('\n')

    index = 0
    steps = 0
    while index != 'escaped':
        index = jump(index, instructions)
        if index != 'escaped':
            steps += 1

    print("Steps: %s" % steps)

if __name__ == '__main__':
    main()
    