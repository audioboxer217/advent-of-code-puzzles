''' Day 8: I Heard You Like Registers
    Part 1 '''

import operator

def convert_comparison(comparison):
    ''' Converts the comparision operator to an operator object '''

    return {
        '<': operator.lt,
        '<=': operator.le,
        '==': operator.eq,
        '!=': operator.ne,
        '>=': operator.ge,
        '>': operator.gt,
    }.get(comparison)

def evaluate_statement(check, compare, value):
    ''' Evaluates the statement '''

    compare = convert_comparison(compare)

    return compare(check, value)

def process_instruction(key, action, amount, check, compare, value, register_dict, largest):
    ''' Processes the current instruction '''

    if key not in register_dict:
        register_dict[key] = 0

    if check not in register_dict:
        register_dict[check] = 0

    if evaluate_statement(register_dict[check], compare, int(value)):
        if action == 'inc':
            register_dict[key] += int(amount)
        elif action == 'dec':
            register_dict[key] -= int(amount)

    if (largest is None) or (register_dict[key] > largest):
        largest = register_dict[key]

    return register_dict, largest

def find_largest_register(register_dict):
    ''' Finds the largest register in the dictionary '''

    largest_val = None
    for key in register_dict:
        if (largest_val is None) or (register_dict[key] > largest_val):
            largest_key = key
            largest_val = register_dict[key]

    largest = {largest_key: largest_val}
    return largest

def main():
    ''' Follow Instructions to update register dictionary '''

    register_dict = {}
    largest_held = None
    with open("../puzzle_input.txt") as file:
        for line in file:
            instruction = line.replace('\n', '').replace('if', '').split()
            register_dict, largest_held = process_instruction(*instruction,
                                                              register_dict,
                                                              largest_held)

    largest_register = find_largest_register(register_dict)

    print("Largest Register: %s" % largest_register)
    print("Largest Value Held: %s" % largest_held)

if __name__ == '__main__':
    main()
    