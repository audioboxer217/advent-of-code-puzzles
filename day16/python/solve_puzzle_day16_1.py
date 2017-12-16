''' Permutation Promenade '''


def spin(members, amount):
    ''' Spin dance members around '''

    return members[-amount:] + members[:-amount]

def exchange(members, mem_a, mem_b):
    ''' Exchange the two given members '''

    mem_a_name = members[mem_a]
    mem_b_name = members[mem_b]

    members[mem_a] = mem_b_name
    members[mem_b] = mem_a_name

    return members

def main():
    ''' Permutation Promenade '''

    programs = list(map(chr, range(ord('a'), ord('p')+1)))

    dance_instructions = open('../puzzle_input.txt').read().split(',')

    for instruction in dance_instructions:
        dance_move = instruction[:1]
        move_inputs = instruction[1:].split('/')

        if dance_move == 's':
            programs = spin(programs, int(move_inputs[0]))
        elif dance_move == 'x':
            prog_a = move_inputs[0]
            prog_b = move_inputs[1]
            programs = exchange(programs, int(prog_a), int(prog_b))
        elif dance_move == 'p':
            prog_a = programs.index(move_inputs[0])
            prog_b = programs.index(move_inputs[1])
            programs = exchange(programs, prog_a, prog_b)
        else:
            print('Error: unknown Dance Move %s' % dance_move)

    print(''.join(programs))
if __name__ == '__main__':
    main()
    