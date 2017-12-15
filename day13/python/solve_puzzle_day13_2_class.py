''' Packet Scanners - Part 2 '''

FIREWALL = ''

class Scanner:
    ''' Firewall Scanners '''

    scanner_range = 0
    layer = 0

    def __init__(self, scanner_range, layer):
        self.scanner_range = scanner_range
        self.layer = layer

    def scanner_at_top(self, time, delay):
        ''' Check if the Scanner is on top for the given layer '''
        return (self.layer+delay) % ((self.scanner_range-1)*2) == 0


def firewall_clearance_attempt(delay):
    ''' Sends a packet through the firewall '''
    for time, position in enumerate(FIREWALL):
        if position.scanner_at_top(time, delay):
            return False

    return True

def main():
    ''' Packet Scanners '''

    global FIREWALL

    scanners = []
    scanner_input = open('../puzzle_input.txt').read().split('\n')
    for details in scanner_input:
        scanner_detail = list(map(int, details.split(": ")))
        scanners.append(scanner_detail)

    FIREWALL = [Scanner(detail[1], detail[0]) for detail in scanners]

    start_time = 0
    while not firewall_clearance_attempt(start_time):
        start_time += 1

    print("Start Time: " + str(start_time))

if __name__ == '__main__':
    main()
    