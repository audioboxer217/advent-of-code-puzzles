''' Hex Ed '''

def movement(direction, axis):
    ''' Determine the movement along an axis for a given direction '''

    return {
        'n':{
            'x': 0,
            'y': 1,
            'z': -1
        },
        'ne':{
            'x': 1,
            'y': 0,
            'z': -1
        },
        'nw':{
            'x': -1,
            'y': 1,
            'z': 0
        },
        's':{
            'x': 0,
            'y': -1,
            'z': 1
        },
        'se':{
            'x': 1,
            'y': -1,
            'z': 0
        },
        'sw':{
            'x': -1,
            'y': 0,
            'z': 1
        }
    }[direction][axis]

def main():
    ''' Hex Ed '''

    file = open("../puzzle_input.txt")
    directions = file.read().split(",")
    position = {'x': 0, 'y': 0, 'z': 0}
    distance = []

    for direction in directions:
        position['x'] += movement(direction, 'x')
        position['y'] += movement(direction, 'y')
        position['z'] += movement(direction, 'z')
        distance.append((abs(-position['x']) + abs(-position['y']) + abs(-position['z']))/2)

    print(int((max(distance))))

if __name__ == '__main__':
    main()
    