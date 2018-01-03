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
  name: valid_passphrase_anagram

  inputs:
    - passphrase

  python_action:
    script: |
        words = passphrase.split()
        valid_passphrase = True
        for word in words:
            letters = list(word)
            anagram_count = 0
            for comp_word in words:
                comp_letters = list(comp_word)
                if sorted(letters) == sorted(comp_letters):
                    anagram_count += 1

            if anagram_count > 1:
                valid_passphrase = False

        if valid_passphrase:
          increase = '1'
        else:
          increase = '0'

  outputs:
    - increase: ${str(increase)}

  results:
    - SUCCESS