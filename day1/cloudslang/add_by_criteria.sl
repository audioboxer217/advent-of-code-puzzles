####################################################
#!!
#! @description: Simple addition of numbers in a list
#!  when two numbers match halfway through the list
#!
#! @input num_list: list of numbers to iterate over
#!
#! @output total: Total of the numbers that match the
#!  criteria
#!
#!!#
####################################################

namespace: cloudslang

operation:
  name: add_by_criteria

  inputs:
    - num_list

  python_action:
    script: |
        key_match = int(len(num_list)/2)
        total = 0
        for index, curr_num in enumerate(num_list):
            if index < key_match:
                halfway = index + key_match
            else:
                halfway = index - key_match

            halfway_num = num_list[halfway]

            if curr_num == halfway_num:
                total += int(curr_num)

  outputs:
    - total: ${str(total)}