####################################################!
#! @input string: input_description
#! @inpu: input_description
#!
#! @output output_name: output_description
#!
#! @result output_description: result_description
#!!#
####################################################

namespace: cloudslang

operation:
  name: get_value

  inputs:
    - row

  python_action:
    script: |
        row = row.split('\t')
        for curr_num in row:
          for num in row:
              if num != curr_num:
                  mod_check = int(curr_num)%int(num)
                  if mod_check == 0:
                      value = int(curr_num)/int(num)

  outputs:
    - smallest
    - largest
    - value: ${str(value)}

  results:
    - SUCCESS