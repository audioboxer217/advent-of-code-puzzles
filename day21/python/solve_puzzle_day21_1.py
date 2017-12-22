''' Fractal Art '''

import numpy as np

def rotate_pattern(pattern):
    ''' Rotate the given pattern '''

    pattern_90 = list(map(list, zip(*pattern[::-1])))
    pattern_180 = list(map(list, zip(*pattern_90[::-1])))
    pattern_270 = list(map(list, zip(*pattern_180[::-1])))
    return [pattern, pattern_90, pattern_180, pattern_270]

def flip_pattern(pattern):
    ''' Flip the given pattern '''

    pattern_1f = list(reversed(pattern))
    pattern_2f = []
    for item in pattern:
        pattern_2f.append(reversed(item))
    return [pattern_1f, pattern_2f]

def compare(pattern_1, pattern_2):
    ''' Compare the given patterns for a match '''
    flipped = flip_pattern(pattern_1)
    patterns = rotate_pattern(pattern_1) + \
        flipped + \
        rotate_pattern(flipped[0]) + \
        rotate_pattern(flipped[1])
    return pattern_2 in patterns

def find_pattern(item, rules):
    ''' Find and apply matching rules'''

    for pattern in rules:
        pattern_1 = []
        for line in pattern[0].split('/'):
            search = list(line)
            pattern_1.append(search)

        if compare(pattern_1, item):
            pattern_2 = []
            for line in pattern[1].split('/'):
                replace = list(line)
                pattern_2.append(replace)
            return pattern_2
    return False

def process_grid(grid, rules):
    ''' Process and grow each grid according to the "rules" '''
    if grid.__len__()%2 == 0:
        grid_divisor = 2
    else:
        grid_divisor = 3

    new_grid = []
    grid_size = int(len(grid) / grid_divisor)
    for y_axis in range(grid_size):
        regions = []
        for x_axis in range(grid_size):
            combined_pattern = []
            for outer in range(grid_divisor):
                sub_pattern = []
                for inner in range(grid_divisor):
                    sub_pattern.append(
                        grid[grid_divisor * y_axis + outer][grid_divisor * x_axis + inner]
                        )
                combined_pattern.append(sub_pattern)
            regions.append(find_pattern(combined_pattern, rules))
        regions = np.hstack(regions).tolist()
        new_grid.extend(regions)
    return new_grid

def main():
    ''' Fractal Art '''

    art = [[".", "#", "."], [".", ".", "#"], ["#", "#", "#"]]
    file = open('../puzzle_input.txt').read().split('\n')

    rules = []
    for rule in file:
        rule = rule.split(' => ')
        rules.append(rule)

    for _ in range(5):
        art = process_grid(art, rules)

    count = 0
    for row in art:
        count += row.count("#")

    print(count)

if __name__ == '__main__':
    main()
    