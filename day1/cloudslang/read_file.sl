####################################################
#!!
#! @description: Operation_description
#!
#! @input filename: input_description
#!
#! @output char_list: output_description
#!
#!!#
####################################################

namespace: cloudslang

operation:
  name: read_file

  inputs:
    - filename

  python_action:
    script: |
        file = open(filename)
        #char_list = list(file.read())
        char_list = file.read()

  outputs:
    - char_list: ${str(char_list)}