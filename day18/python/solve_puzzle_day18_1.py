''' Duet '''

REGISTER = {}

def get_instruction_detail(instruction_arr):
    ''' Splits the Instruction array and returns the relevent values '''

    instruction = instruction_arr[0]
    note = instruction_arr[1]
    if len(instruction_arr) == 3:
        try:
            value = int(instruction_arr[2])
        except ValueError:
            value = int(REGISTER[instruction_arr[2]])
    else:
        value = None

    return instruction, note, value

def play_sound(note):
    ''' plays a sound with a frequency equal to the value of 'note'. '''

    return REGISTER[note]

def set_register(note, value):
    ''' sets 'note' to the value of 'value'. '''
    global REGISTER

    REGISTER[note] = value

def increase_register(note, value):
    ''' increases 'note' by the value of 'value'. '''
    global REGISTER

    REGISTER[note] += value

def multiply_register(note, value):
    ''' sets note to the result of multiplying the value of 'note'
        by the value of 'value'. '''

    global REGISTER

    REGISTER[note] *= value

def modulate_register(note, value):
    ''' sets 'note' to the remainder of dividing the value contained
        in 'note' by the value of 'value' (that is, it sets 'note' to
        the result of 'note' modulo 'value'). '''

    global REGISTER

    REGISTER[note] %= value

def recover_register(note, last_frequency):
    ''' recovers the frequency of the last sound played, but only when
        the value of 'note' is not zero. (If it is zero, the command does nothing.) '''

    global REGISTER

    if REGISTER[note] != 0:
        REGISTER[note] = last_frequency
        return True

def jump_instructions(note):
    ''' jumps with an offset of the value of 'value', but only if the value of 'note'
        is greater than zero. (An offset of 2 skips the next instruction, an offset
        of -1 jumps to the previous instruction, and so on.) '''

    if REGISTER[note] > 0:
        return True

def main():
    ''' Duet '''

    frequency = 0

    instructions = open('../puzzle_input.txt').read().split('\n')
    inst_length = len(instructions)

    i = 0
    while i < inst_length:
        instruction_arr = instructions[i].split(' ')
        instruction, note, value = get_instruction_detail(instruction_arr)

        if note not in REGISTER:
            REGISTER[note] = 0

        if instruction == 'snd':
            frequency = play_sound(note)
            i += 1
        elif instruction == 'set':
            set_register(note, value)
            i += 1
        elif instruction == 'add':
            increase_register(note, value)
            i += 1
        elif instruction == 'mul':
            multiply_register(note, value)
            i += 1
        elif instruction == 'mod':
            modulate_register(note, value)
            i += 1
        elif instruction == 'rcv':
            if recover_register(note, frequency):
                break
            else:
                i += 1
        elif instruction == 'jgz':
            if jump_instructions(note):
                i += value
            else:
                i += 1

    print(frequency)


if __name__ == '__main__':
    main()
    