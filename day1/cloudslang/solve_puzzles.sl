####################################################
#!!
#! @description: Flow_description
#!
#! @input filename: 
#!
#! @output output_name: output_description
#!
#! @result result_name: result_description
#!!#
####################################################

namespace: cloudslang

flow:
  name: solve_puzzles

  inputs:
    - filename

  workflow:
    - read_file:
        do:
          cloudslang.read_file:
            - filename
        publish:
          - num_list: ${char_list}
        navigate:
          - SUCCESS: add_duplicates
    
    - add_duplicates:
        do:
          cloudslang.add_duplicates:
            - num_list
        publish:
          - solution1: ${total}
        navigate:
          - SUCCESS: add_by_criteria
    
    - add_by_criteria:
        do:
          cloudslang.add_by_criteria:
            - num_list
        publish:
          - solution2: ${total}
        navigate:
          - SUCCESS: SUCCESS

  outputs:
    - solution1: ${solution1}
    - solution2: ${solution2}

  results:
    - SUCCESS