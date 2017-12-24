''' Coprocessor Conflagration '''

import math

def is_prime(num):
    ''' Determine if number is prime '''

    ans = True
    for i in range(2, int(math.sqrt(num))):
        if num % i == 0:
            ans = False
            break
    return ans

def main():
    ''' Coprocessor Conflagration '''

    reg_h = 0
    reg_b = 81          # first instruction for 'b'
    reg_b *= 100        # second instruction for 'b'
    reg_b += 100000     # third instruction for 'b'
    reg_c = reg_b       # second instruction for 'c' (first was the same)
    reg_c += 17000      # third instruction for 'c'

    for i in range(reg_b, reg_c+1, 17):
        if not is_prime(i):
            reg_h = reg_h + 1

    print(reg_h)

if __name__ == '__main__':
    main()
    