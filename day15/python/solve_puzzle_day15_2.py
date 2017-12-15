''' Dueling Generators '''

A_FACTOR = 16807
A_QC = 4
B_FACTOR = 48271
B_QC = 8
DEVISOR = 2147483647

def generate_next_value(value, factor):
    ''' Generate the next value for each generator '''

    value *= factor
    value %= DEVISOR

    return value

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

    for _ in range(5000000):
        a_qual_check = False
        while not a_qual_check:
            gen_a = generate_next_value(gen_a, A_FACTOR)
            if gen_a % A_QC == 0:
                a_qual_check = True

        b_qual_check = False
        while not b_qual_check:
            gen_b = generate_next_value(gen_b, B_FACTOR)
            if gen_b % B_QC == 0:
                b_qual_check = True

        if check_for_match(gen_a, gen_b):
            pairs += 1

    print(pairs)

if __name__ == '__main__':
    main()
    