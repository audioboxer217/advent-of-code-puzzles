''' Dueling Generators '''

A_FACTOR = 16807
B_FACTOR = 48271
DEVISOR = 2147483647

def generate_next_value(gen_a, gen_b):
    ''' Generate the next value for each generator '''

    gen_a *= A_FACTOR
    gen_a %= DEVISOR

    gen_b *= B_FACTOR
    gen_b %= DEVISOR

    return gen_a, gen_b

def check_for_match(gen_a, gen_b):
    ''' Check the last 16 bits of each generators value for a match '''

    if gen_a & 0xFFFF == gen_b & 0xFFFF:
        return True


def main():
    ''' Dueling Generators '''

    generators = []
    with open("../puzzle_input.txt") as file:
        for line in file:
            generators.append(int(line.split(" ")[4]))

    gen_a = generators[0]
    gen_b = generators[1]
    pairs = 0

    for _ in range(40000000):
        gen_a, gen_b = generate_next_value(gen_a, gen_b)
        if check_for_match(gen_a, gen_b):
            pairs += 1

    print(pairs)

if __name__ == '__main__':
    main()
    