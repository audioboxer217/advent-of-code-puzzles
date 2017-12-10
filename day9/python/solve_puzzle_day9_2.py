''' Proccess Stream '''

def main():
    ''' Proccess Stream '''

    total_score = []
    group_score = 0
    garbage_count = 0
    ignore = False
    garbage = False

    file = open("../puzzle_input.txt")
    for char in file.read():
        if ignore:
            ignore = False
            continue
        elif char == '!':
            ignore = True
            continue
        elif garbage:
            if char == '>':
                garbage = False
            else:
                garbage_count += 1
                continue
        elif char == '{':
            group_score += 1
            total_score.append(group_score)
            continue
        elif char == '<':
            garbage = True
            continue
        elif char == '}':
            group_score -= 1
            continue

    print("Total Score: %s" % sum(total_score))
    print("Garbage: %s" % garbage_count)

if __name__ == '__main__':
    main()
    