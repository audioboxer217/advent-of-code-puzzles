''' Duet '''

INSTRUCTIONS = open('../puzzle_input.txt').read().split('\n')
REGISTER = [{'p': 0}, {'p': 1}]
QUEUE = [[], []]
POINTER = [0, 0]
COUNTER = [0, 0]

def get_value(item, reg_id):
    ''' Splits the Instruction array and returns the relevent values '''

    global REGISTER

    try:
        int(item)
    except ValueError:
        if item not in REGISTER[reg_id]:
            REGISTER[reg_id][item] = 0
        return REGISTER[reg_id][item]

    return int(item)

def send(value1, reg_id):
    ''' Sends a value2 to the queue. '''
    global QUEUE
    global POINTER
    global COUNTER

    QUEUE[reg_id-1].append(get_value(value1, reg_id))
    POINTER[reg_id] += 1
    COUNTER[reg_id] += 1

def set_register(value1, value2, reg_id):
    ''' sets 'value1' to the value2 of 'value2'. '''
    global REGISTER
    global POINTER

    REGISTER[reg_id][value1] = get_value(value2, reg_id)
    POINTER[reg_id] += 1

def increase_register(value1, value2, reg_id):
    ''' increases 'value1' by the value2 of 'value2'. '''
    global REGISTER
    global POINTER

    REGISTER[reg_id][value1] = get_value(value1, reg_id) + get_value(value2, reg_id)
    POINTER[reg_id] += 1

def multiply_register(value1, value2, reg_id):
    ''' sets value1 to the result of multiplying the value2 of 'value1'
        by the value2 of 'value2'. '''

    global REGISTER
    global POINTER

    REGISTER[reg_id][value1] = get_value(value1, reg_id) * get_value(value2, reg_id)
    POINTER[reg_id] += 1

def modulate_register(value1, value2, reg_id):
    ''' sets 'value1' to the remainder of dividing the value2 contained
        in 'value1' by the value2 of 'value2' (that is, it sets 'value1' to
        the result of 'value1' modulo 'value2'). '''

    global REGISTER
    global POINTER

    REGISTER[reg_id][value1] = get_value(value1, reg_id) % get_value(value2, reg_id)
    POINTER[reg_id] += 1

def receive(value1, reg_id):
    ''' recovers the frequency of the last sound played, but only when
        the value2 of 'value1' is not zero. (If it is zero, the command does nothing.) '''

    global REGISTER
    global QUEUE
    global POINTER

    if len(QUEUE[reg_id]) > 0:
        REGISTER[reg_id][value1] = QUEUE[reg_id][0]
        QUEUE[reg_id].pop(0)
        POINTER[reg_id] += 1
        return True
    else:
        return False

def jump_instructions(value1, value2, reg_id):
    ''' jumps with an offset of the value2 of 'value2', but only if the value2 of 'value1'
        is greater than zero. (An offset of 2 skips the next instruction, an offset
        of -1 jumps to the previous instruction, and so on.) '''

    global POINTER

    if get_value(value1, reg_id) > 0:
        POINTER[reg_id] += get_value(value2, reg_id)
    else:
        POINTER[reg_id] += 1

def run_program_step(reg_id):
    ''' Runs the program for the register with the given ID '''

    step = POINTER[reg_id]

    if step >= len(INSTRUCTIONS):
        return False

    if step < 0:
        step = len(INSTRUCTIONS)
        return False

    instruction_arr = INSTRUCTIONS[step].split(' ')
    instruction = instruction_arr[0]
    value1 = instruction_arr[1]
    if len(instruction_arr) == 3:
        value2 = instruction_arr[2]

    if instruction == 'snd':
        send(value1, reg_id)
        return True
    elif instruction == 'set':
        set_register(value1, value2, reg_id)
        return True
    elif instruction == 'add':
        increase_register(value1, value2, reg_id)
        return True
    elif instruction == 'mul':
        multiply_register(value1, value2, reg_id)
        return True
    elif instruction == 'mod':
        modulate_register(value1, value2, reg_id)
        return True
    elif instruction == 'rcv':
        if receive(value1, reg_id):
            return True
        else:
            return False
    elif instruction == 'jgz':
        jump_instructions(value1, value2, reg_id)
        return True

def main():
    ''' Duet '''

    while True:
        while run_program_step(0):
            pass
        while run_program_step(1):
            pass

        if len(QUEUE[0]) == 0 and len(QUEUE[1]) == 0:
            break
        if POINTER[0] >= len(INSTRUCTIONS) and POINTER[1] >= len(INSTRUCTIONS):
            break

    print(str(COUNTER[1]))

if __name__ == '__main__':
    main()
    