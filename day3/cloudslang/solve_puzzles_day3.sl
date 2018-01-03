####################################################
#!!
#! @description: Flow_description
#!
#! @input input_name: input_description
#! @input input_name: input_description
#!
#! @output output_name: output_description
#!
#! @result result_name: result_description
#!!#
####################################################

namespace: cloudslang

flow:
  name: solve_puzzles_day3

  inputs:
    - square_num

  workflow:
    - count_steps:
        do:
          count_steps:
            - square_num
        publish:
          - steps
        navigate:
          - SUCCESS: find_next_largest_value

    - find_next_largest_value:
        do:
          find_next_largest_value:
            - square_num
        publish:
          - next_largest_value
        navigate:
          - SUCCESS: SUCCESS

  outputs:
    - steps
    - next_largest_value

  results:
    - SUCCESS