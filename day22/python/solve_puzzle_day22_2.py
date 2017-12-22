''' Sporifica Virus '''

def determine_start(grid_map):
    ''' Determine the starting position '''

    y_len = len(grid_map)
    x_len = len(grid_map[0])

    y_axis = y_len // 2
    x_axis = x_len // 2

    return x_axis, y_axis

def determine_direction(state):
    ''' Determine the direction to turn the virus carrier '''

    return{
        '.': 'left',
        'W': 'none',
        '#': 'right',
        'F': 'reverse'
    }[state]

def turn_carrier(state, direction):
    ''' Turn the virus carrier '''

    turn = determine_direction(state)

    return {
        'N': {'left': 'W', 'right': 'E', 'reverse': 'S', 'none': 'N'},
        'S': {'left': 'E', 'right': 'W', 'reverse': 'N', 'none': 'S'},
        'E': {'left': 'N', 'right': 'S', 'reverse': 'W', 'none': 'E'},
        'W': {'left': 'S', 'right': 'N', 'reverse': 'E', 'none': 'W'},
    }[direction][turn]

def change_node(state):
    ''' Change the node to infected/cleaned '''

    return {
        '.': 'W',
        'W': '#',
        '#': 'F',
        'F': '.'
    }[state]

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
    for _ in range(10000000):
        state = grid_map[y_axis][x_axis]
        if state == 'W':
            count += 1
        direction = turn_carrier(state, direction)
        grid_map[y_axis][x_axis] = change_node(state)
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
    