####################################################
#!!
#! @description: Simple addition of numbers in a list
#!  when there are two consecutive nubmers
#!
#! @input filename: File containing the list of numbers
#!
#! @output total: Total of the numbers that match the
#!  criteria
#!
#! @result output_description: result_description
#!!#
####################################################

namespace: cloudslang

operation:
  name: add_duplicates

  inputs:
    - num_list

  python_action:
    script: |
        first_num = num_list[0]
        total = 0
        for index, curr_num in enumerate(num_list):
            if 'last_num' in locals():
                if curr_num == last_num:
                    total += int(curr_num)
                last_num = curr_num
            else:
                last_num = first_num
        if last_num == first_num:
            total += int(first_num)

  outputs:
    - total: ${str(total)}