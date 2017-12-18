''' Spinlock  '''

def main():
    ''' Spinlock  '''

    spinlock = [0]
    steps = 337
    position = 0

    insertion = 1
    while insertion <= 2017:
        spinlock_size = len(spinlock)
        insertion_point = ((position + steps) % spinlock_size) + 1
        spinlock.insert(insertion_point, insertion)
        insertion += 1
        position = insertion_point

    answer = spinlock.index(2017) + 1
    print(spinlock[answer])

if __name__ == '__main__':
    main()
    