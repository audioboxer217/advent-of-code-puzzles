''' Spinlock  '''

def main():
    ''' Spinlock  '''

    steps = 337
    position = 0
    length = 1

    for i in range(1, int(50e6) + 1):
        position = ((position + steps) % length) + 1
        if position == 1:
            answer = i
        length += 1

    print(answer)

if __name__ == '__main__':
    main()
    