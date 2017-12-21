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
  name: get_span

  inputs:
    - row

  python_action:
    script: |
        row = row.split('\t')
        smallest = row[0]
        largest = row[0]
        for curr_num in row:
            if int(curr_num) < int(smallest):
                smallest = curr_num
            if int(curr_num) > int(largest):
                largest = curr_num
        
        difference = int(largest) - int(smallest)

  outputs:
    - smallest
    - largest
    - difference: ${str(difference)}

  results:
    - SUCCESS