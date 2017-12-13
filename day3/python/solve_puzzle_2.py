''' Spiral Memory '''

# constants
DIR_RIGHT = 0
DIR_UP = 1
DIR_LEFT = 2
DIR_DOWN = 3

def find_next_largest_value(square_num, grid_size):
    ''' Find the next largest value after the given square number '''

    tab = [[0]*grid_size for _ in range(0, grid_size)]

    y_axis = int(grid_size/2)
    x_axis = y_axis+1

    tab[y_axis][x_axis-1] = 1       # initial value

    direction = 0
    max_steps = 1
    steps = 0
    dir_changes = 0

    while x_axis <= grid_size and y_axis <= grid_size:
        tab[y_axis][x_axis] += (tab[y_axis-1][x_axis-1] if y_axis > 0 and x_axis > 0 else 0) + \
                                (tab[y_axis-1][x_axis] if y_axis > 0 else 0) + \
                                (tab[y_axis-1][x_axis+1] if y_axis > 0 and x_axis < grid_size else 0)
        tab[y_axis][x_axis] += (tab[y_axis][x_axis-1] if x_axis > 0 else 0) + \
                                (tab[y_axis][x_axis+1] if x_axis < grid_size else 0)
        tab[y_axis][x_axis] += (tab[y_axis+1][x_axis-1] if y_axis < grid_size and x_axis > 0 else 0) + \
                                (tab[y_axis+1][x_axis] if y_axis < grid_size else 0) + \
                                (tab[y_axis+1][x_axis+1] if y_axis < grid_size and x_axis < grid_size else 0)

        if tab[y_axis][x_axis] > square_num:
            next_largest_value = tab[y_axis][x_axis]
            return next_largest_value

        steps = steps+1
        if steps == max_steps:
            dir_changes = dir_changes+1
            direction = (direction+1)%4
            steps = 0
            if dir_changes%2 == 0:
                max_steps = max_steps+1

        if direction == DIR_RIGHT:
            x_axis = x_axis+1
        if direction == DIR_UP:
            y_axis = y_axis+1
        if direction == DIR_LEFT:
            x_axis = x_axis-1
        if direction == DIR_DOWN:
            y_axis = y_axis-1

def main():
    ''' Spiral Memory '''

    square_num = 289326
    grid_size = 20

    answer = find_next_largest_value(square_num, grid_size)
    print(answer)
if __name__ == '__main__':
    main()
    