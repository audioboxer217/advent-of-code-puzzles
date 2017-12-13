''' Digital Plumber '''

def associate_pipes(program, associations):
    ''' Completes the path assocations for a program '''

    i = 0

    while i < len(program):
        for item in associations:
            if program[i] in item:
                program = list(set(program + item))
                associations.remove(item)
                i = 0
        i += 1

    return program, associations

def main():
    ''' Digital Plumber '''

    associations = []
    with open("../puzzle_input.txt") as file:
        for line in file:
            associations.append(list(map(int, (line.split(" <-> "))[1].split(", "))))

    for idx, item in enumerate(associations):
        associations[idx] = (list(set(item+[idx])))

    pipes = []
    while len(associations) > 0:
        program, associations = associate_pipes(associations[0], associations)
        pipes.append(program)

    for pipe in pipes:
        if 0 in pipe:
            print(len(pipe))

if __name__ == '__main__':
    main()
    