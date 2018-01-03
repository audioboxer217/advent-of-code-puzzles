####################################################
#!!
#! @description: Operation_description
#!
#! @input passphrase: input_description
#! @input input_name: input_description
#!
#! @output output_name: output_description
#!
#! @result output_description: result_description
#!!#
####################################################

namespace: cloudslang

operation:
  name: valid_passphrase_simple

  inputs:
    - passphrase

  python_action:
    script: |
        words = passphrase.split()

        valid_passphrase = True
        for word in words:
            word_count = words.count(word)
            if word_count > 1:
                valid_passphrase = False

        if valid_passphrase:
          increase = '1'
        else:
          increase = '0'

  outputs:
    - increase: ${str(increase)}

  results:
    - SUCCESS