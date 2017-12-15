''' Packet Scanners - Part 1 '''

SCANNERS = {}
FIREWALL_SIZE = 0

def create_scanners():
    ''' Create a dictionary of the Scanners from the given details '''

    global FIREWALL_SIZE
    scanner_details = open('../puzzle_input.txt').read().split('\n')

    for scanner in scanner_details:
        scanner = scanner.split(': ')
        scanner_depth = int(scanner[0])
        scanner_range = int(scanner[1])
        SCANNERS[scanner_depth] = {'range': scanner_range, 'position': 0, 'movement': 'down'}

    sorted_scanners = sorted(iter(SCANNERS.keys()))
    FIREWALL_SIZE = sorted_scanners[-1]

    for depth in range(FIREWALL_SIZE):
        if depth not in SCANNERS:
            SCANNERS[depth] = {'range': 0, 'position': -1, 'movement': 'none'}

def check_for_hit(picosecond):
    ''' Check if any scanners caught the packet '''

    if SCANNERS[picosecond]['position'] == 0:
        return True
    else:
        return False
    # return bool(SCANNERS[picosecond]['position'] == 0)

def move_scanners():
    ''' Move all scanners one step '''

    for key in iter(SCANNERS):
        if SCANNERS[key]['movement'] == 'down':
            SCANNERS[key]['position'] += 1
        elif SCANNERS[key]['movement'] == 'up':
            SCANNERS[key]['position'] -= 1
        else: continue
        if SCANNERS[key]['position'] == SCANNERS[key]['range']-1:
            SCANNERS[key]['movement'] = 'up'
        elif SCANNERS[key]['position'] == 0:
            SCANNERS[key]['movement'] = 'down'

def reset_scanners():
    ''' Reset all scanners to 0 '''

    for key in range(FIREWALL_SIZE + 1):
        if SCANNERS[key]['range'] > 0:
            SCANNERS[key]['position'] = 0
            SCANNERS[key]['movement'] = 'down'

def firewall_clearance_attempt(start_time):
    ''' Attempt to pass through the firewall without being caught '''

    reset_scanners()

    for picosecond in range(0, start_time):
        move_scanners()
        picosecond += 1

    for picosecond in range(0, FIREWALL_SIZE + 1):
        full_time = picosecond + start_time
        if check_for_hit(picosecond):
            print("Caught at layer %s in %s picoseconds" % (picosecond, full_time))
            return False
        move_scanners()
        picosecond += 1

    return True

def main():
    ''' Packet Scanners '''

    create_scanners()

    start_time = 0
    while not firewall_clearance_attempt(start_time):
        print("Attempt %s" % start_time)
        start_time += 1
    print(start_time)

if __name__ == '__main__':
    main()
    