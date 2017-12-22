''' Sporifica Virus '''

def determine_start(grid_map):
    ''' Determine the starting position '''

    y_len = len(grid_map)
    x_len = len(grid_map[0])

    y_axis = y_len // 2
    x_axis = x_len // 2

    return x_axis, y_axis

def turn_carrier(infected, direction):
    ''' Determine the direction to turn the virus carrier '''

    if infected:
        turn = 'right'
    else:
        turn = 'left'

    return {
        'N': {'left': 'W', 'right': 'E'},
        'S': {'left': 'E', 'right': 'W'},
        'E': {'left': 'N', 'right': 'S'},
        'W': {'left': 'S', 'right': 'N'},
    }[direction][turn]

def change_node(infected, grid_map, x_axis, y_axis):
    ''' Change the node to infected/cleaned '''

    if infected:
        grid_map[y_axis][x_axis] = '.'
    else:
        grid_map[y_axis][x_axis] = '#'

    return grid_map

def move_node(direction, x_axis, y_axis):
    ''' Move the virus carrier in the grid '''

    return {
        'N': [x_axis, y_axis - 1],
        'S': [x_axis, y_axis + 1],
        'E': [x_axis + 1, y_axis],
        'W': [x_axis - 1, y_axis]
    }[direction]

def grow_grid(grid_map, side):
    ''' Grows the Grid as needed '''

    if (side == 'top') or (side == 'bottom'):
        x_len = len(grid_map[0])
        if side == 'top':
            grid_map.insert(0, ['.'] * x_len)
        else:
            grid_map.append(['.'] * x_len)

    else:
        for row, _ in enumerate(grid_map):
            if side == 'left':
                grid_map[row].insert(0, '.')
            else:
                grid_map[row].append('.')

    return grid_map

def main():
    ''' Sporifica Virus '''

    file = open('../puzzle_input.txt').read().split('\n')

    grid_map = []
    for line in file:
        grid_map.append(list(line))

    x_axis, y_axis = determine_start(grid_map)
    direction = 'N'

    count = 0
    for _ in range(10000):
        infected = bool(grid_map[y_axis][x_axis] == '#')
        if not infected:
            count += 1
        direction = turn_carrier(infected, direction)
        grid_map = change_node(infected, grid_map, x_axis, y_axis)
        x_axis, y_axis = move_node(direction, x_axis, y_axis)
        if y_axis < 0:
            grid_map = grow_grid(grid_map, 'top')
            y_axis = 0
        elif y_axis == len(grid_map):
            grid_map = grow_grid(grid_map, 'bottom')
        elif x_axis < 0:
            grid_map = grow_grid(grid_map, 'left')
            x_axis = 0
        elif x_axis == len(grid_map[0]):
            grid_map = grow_grid(grid_map, 'right')

    print(count)

if __name__ == '__main__':
    main()
    