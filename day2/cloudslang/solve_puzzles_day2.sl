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

imports:
  cloudslang: cloudslang
  filesystem: io.cloudslang.base.filesystem
  print: io.cloudslang.base.print

flow:
  name: solve_puzzles_day2

  inputs:
    - file_path
    - checksum_1:
        required: true
        default: '0'
        private: true
    - checksum_2:
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
          - SUCCESS: calculate_checksum_1
          - FAILURE: FAILURE

    - calculate_checksum_1:
        loop:
          for: line in read_text.split('\n')
          do:
            cloudslang.get_span:
              - row: ${line}
              - checksum_1
          publish:
            - checksum_1: ${str(int(checksum_1) + int(difference))}
          break: []
        navigate:
          - SUCCESS: calculate_checksum_2

    - calculate_checksum_2:
        loop:
          for: line in read_text.split('\n')
          do:
            cloudslang.get_value:
              - row: ${line}
              - checksum_2
          publish:
            - checksum_2: ${str(int(checksum_2) + int(value))}
          break: []
        navigate:
          - SUCCESS: SUCCESS

  outputs:
    - puzzle_1: ${checksum_1}
    - puzzle_2: ${checksum_2}

  results:
    - SUCCESS
    - FAILURE