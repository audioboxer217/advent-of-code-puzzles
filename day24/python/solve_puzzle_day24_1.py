''' Electromagnetic Moat '''

import numpy as np

def build_bridge(parts, port, weight, i):
    ''' Build a bridge with possible solutions '''

    bridge = []
    i += 1
    matches = np.where(np.array(parts) == port)[0].tolist()
    if matches:
        for index in matches:
            curr_part = parts[index]
            next_port = curr_part[curr_part.index(port)-1]
            tmp_parts = []
            for part in parts:
                if part != curr_part:
                    tmp_parts.append(part)
            bridge.extend(build_bridge(tmp_parts, next_port, weight + sum(curr_part), i+1))
        return bridge
    else:
        return [[weight, i]]

def main():
    ''' Electromagnetic Moat '''

    parts = open('../puzzle_input.txt').read().split('\n')
    for i, _ in enumerate(parts):
        parts[i] = list(map(int, parts[i].split("/")))

    bridges = build_bridge(parts, 0, 0, 0)

    strongest = 0
    for weights in bridges:
        if weights[0] > strongest:
            strongest = weights[0]

    print(strongest)

if __name__ == '__main__':
    main()
    