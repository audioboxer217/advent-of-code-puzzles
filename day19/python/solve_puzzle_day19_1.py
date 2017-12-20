''' A Series of Tubes '''

def move_packet(direction, x_axis, y_axis):
    ''' Move the Packet in the Diagram '''

    return {
        'up': [x_axis, y_axis - 1],
        'down': [x_axis, y_axis + 1],
        'left': [x_axis - 1, y_axis],
        'right': [x_axis + 1, y_axis]
    }[direction]

def continue_direction(direction, diagram, x_axis, y_axis):
    ''' Checks to see if a change of direction is needed '''

    if direction == 'up':
        if y_axis > 0:
            if (diagram[y_axis - 1][x_axis] == '|') or (diagram[y_axis - 1][x_axis].isalpha()):
                return True
    elif direction == 'down':
        if y_axis < len(diagram) - 1:
            if (diagram[y_axis + 1][x_axis] == '|') or (diagram[y_axis + 1][x_axis].isalpha()):
                return True
    elif direction == 'left':
        if x_axis > 0:
            if (diagram[y_axis][x_axis - 1] == '-') or (diagram[y_axis][x_axis - 1].isalpha()):
                return True
    elif direction == 'right':
        if x_axis < len(diagram[0]) - 1:
            if (diagram[y_axis][x_axis + 1] == '-') or (diagram[y_axis][x_axis + 1].isalpha()):
                return True

    return False

def change_direction(direction, diagram, x_axis, y_axis):
    ''' Determine the next direction to take. '''

    new_direction = 'none'
    if direction == 'up' or direction == 'down':
        if x_axis > 0:
            if (diagram[y_axis][x_axis - 1] == '-') or (diagram[y_axis][x_axis - 1].isalpha()):
                new_direction = 'left'

        if x_axis < len(diagram[0]) - 1:
            if (diagram[y_axis][x_axis + 1] == '-') or (diagram[y_axis][x_axis + 1].isalpha()):
                new_direction = 'right'

    elif direction == 'right' or direction == 'left':
        if y_axis > 0:
            if (diagram[y_axis - 1][x_axis] == '|') or (diagram[y_axis - 1][x_axis].isalpha()):
                new_direction = 'up'

        if y_axis < len(diagram) - 1:
            if (diagram[y_axis + 1][x_axis] == '|') or (diagram[y_axis + 1][x_axis].isalpha()):
                new_direction = 'down'
    return new_direction

def main():
    ''' A Series of Tubes '''

    diagram = open('../puzzle_input.txt').read().split('\n')

    x_axis = diagram[0].index('|')
    y_axis = 0
    direction = 'down'
    diagram_end = False
    letters = []

    while not diagram_end:
        while True:
            if diagram[y_axis][x_axis] not in ['|', '-', '+']:
                if diagram[y_axis][x_axis].isalpha():
                    letters.append(diagram[y_axis][x_axis])
                else:
                    diagram_end = True
                    break

            x_axis, y_axis = move_packet(direction, x_axis, y_axis)

            if x_axis < 0 or x_axis >= len(diagram[0]) or y_axis < 0 or y_axis >= len(diagram):
                diagram_end = True
                break
            if diagram[y_axis][x_axis] == "+":
                if continue_direction(direction, diagram, x_axis, y_axis):
                    continue
                else:
                    break

        direction = change_direction(direction, diagram, x_axis, y_axis)
        if direction == 'none':
            diagram_end = True

    print(''.join(letters))

if __name__ == '__main__':
    main()
    