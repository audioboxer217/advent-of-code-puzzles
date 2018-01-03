####################################################
#!!
#! @description: Operation_description
#!
#! @input sqaure_numiption
#! @inpuinput_description
#!
#! @output output_name: output_description
#!
#! @result output_description: result_description
#!!#
####################################################

namespace: cloudslang

operation:
  name: count_steps

  inputs:
    - square_num

  python_action:
    script: |
        square_num = int(square_num)

        dir_right = 0
        dir_up = 1
        dir_left = 2
        dir_down = 3

        y_axis = 0
        x_axis = 0

        direction = 0
        max_steps = 1
        steps = 0
        dir_changes = 0

        for _ in range(1, square_num):
            if direction == dir_right:
                x_axis = x_axis+1
            if direction == dir_up:
                y_axis = y_axis+1
            if direction == dir_left:
                x_axis = x_axis-1
            if direction == dir_down:
                y_axis = y_axis-1

            steps = steps+1
            if steps == max_steps:
                dir_changes = dir_changes+1
                direction = (direction+1)%4
                steps = 0
                if dir_changes%2 == 0:
                    max_steps = max_steps+1

  outputs:
    - steps: ${str(abs(x_axis) + abs(y_axis))}


  results:
    - SUCCESS