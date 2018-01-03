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
  name: check_passphrase

  inputs:
    - passphrase

  workflow:
    - valid_passphrase_simple:
        do:
          cloudslang.valid_passphrase_simple:
            - passphrase
        publish: 
          - simple_increase: ${increase}
        navigate:
          - SUCCESS: valid_passphrase_anagram

    - valid_passphrase_anagram:
        do:
          cloudslang.valid_passphrase_anagram:
            - passphrase
        publish: 
          - anagram_increase: ${increase}
        navigate:
          - SUCCESS: SUCCESS

  outputs:
    - simple_increase
    - anagram_increase

  results:
    - SUCCESS