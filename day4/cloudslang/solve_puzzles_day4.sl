####################################################
#!!
#! @description: Flow_description
#!
#! @input file_path: input_description
#! @inpu: input_description
#!
#! @output result: output_description
#!
#! @result SUCCESS: result_description
#!!#
####################################################

namespace: cloudslang

imports:
  filesystem: io.cloudslang.base.filesystem

flow:
  name: solve_puzzles_day4

  inputs:
    - file_path
    - valid_simple_count:
        required: true
        default: '0'
        private: true
    - valid_anagram_count:
        required: true
        default: '0'
        private: true

  workflow:
    - read_file:
        do:
          filesystem.read_from_file:
            - file_path
        publish:
          - read_text
        navigate:
          - SUCCESS: check_passphrase_simple
          - FAILURE: FAILURE
    
    - check_passphrase_simple:
        loop:
          for: line in read_text.split('\n')
          do:
            cloudslang.check_passphrase:
              - passphrase: ${line}
              - valid_simple_count
              - valid_anagram_count
          publish: 
            - valid_simple_count: ${str(int(valid_simple_count) + int(simple_increase))}
            - valid_anagram_count: ${str(int(valid_anagram_count) + int(anagram_increase))}
          break: []
        navigate:
          - SUCCESS: SUCCESS

  outputs:
    - puzzle1: ${valid_simple_count}
    - puzzle2: ${valid_anagram_count}

  results:
    - SUCCESS
    - FAILURE