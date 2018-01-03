####################################################
#!!
#! @description: Operation_description
#!
#! @input square_numiption
#! @input input_name: input_description
#!
#! @output output_name: output_description
#!
#! @result output_description: result_description
#!!#
####################################################

namespace: cloudslang

operation:
  name: find_next_largest_value

  inputs:
    - square_num
    - grid_size:
        required: true
        default: '20'
        private: false

  python_action:
    script: |
        square_num = int(square_num)
        grid_size = int(grid_size)

        dir_right = 0
        dir_up = 1
        dir_left = 2
        dir_down = 3

        tab = [[0]*grid_size for _ in range(0, grid_size)]

        y_axis = int(grid_size/2)
        x_axis = y_axis+1

        tab[y_axis][x_axis-1] = 1       # initial value

        direction = 0
        max_steps = 1
        steps = 0
        dir_changes = 0

        while x_axis <= grid_size and y_axis <= grid_size:
            print('X: %s' % x_axis)
            print('Y: %s' % y_axis)
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
                break

            steps = steps+1
            if steps == max_steps:
                dir_changes = dir_changes+1
                direction = (direction+1)%4
                steps = 0
                if dir_changes%2 == 0:
                    max_steps = max_steps+1

            if direction == dir_right:
                x_axis = x_axis+1
            if direction == dir_up:
                y_axis = y_axis+1
            if direction == dir_left:
                x_axis = x_axis-1
            if direction == dir_down:
                y_axis = y_axis-1

  outputs:
    - next_largest_value: ${str(next_largest_value)}

  results:
    - SUCCESS