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

def dance(programs, dance_instructions):
    ''' Perform the Dance '''

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

    return programs

def determine_dance_loop(dance_instructions):
    ''' Look for the loop where the dance starts over '''

    dance_members = list(map(chr, range(ord('a'), ord('p')+1)))
    dance_loop = []
    dance_members = dance(dance_members, dance_instructions)
    while True:
        dance_members = dance(dance_members, dance_instructions)
        if tuple(dance_members) in dance_loop:
            break
        dance_loop.append(tuple(dance_members))

    return len(dance_loop)


def main():
    ''' Permutation Promenade '''

    dance_instructions = open('../puzzle_input.txt').read().split(',')

    dance_loop_size = determine_dance_loop(dance_instructions)

    programs = list(map(chr, range(ord('a'), ord('p')+1)))
    for _ in range((1000000000) % dance_loop_size):
        programs = dance(programs, dance_instructions)
        print(''.join(programs))
        

    ''' orig_programs = list(map(chr, range(ord('a'), ord('e')+1)))

    programs_final = [None] * len(programs)
    for char in orig_programs:
        orig_pos = orig_programs.index(char)
        new_pos = programs.index(char)
        movement = (new_pos + 1) - (orig_pos + 1)
        if movement < 0:
            movement = len(programs) - ((orig_pos + 1) - (new_pos + 1))
        final_pos = (orig_pos + (movement * 2)) % len(programs)
        programs_final[final_pos] = char
        print('%s: %s -> %s = %s' % (char, orig_pos, new_pos, movement)) '''

    print(''.join(programs))

if __name__ == '__main__':
    main()
    