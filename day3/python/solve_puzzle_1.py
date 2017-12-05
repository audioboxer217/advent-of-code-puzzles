''' Calculate Steps '''

from math import sqrt, floor, ceil

def create_circle(size):
    ''' Calculate the size of "Sprial" '''

    sqr_root = ceil(sqrt(size))
    diameter = sqr_root + 1 if sqr_root % 2 == 0 else sqr_root
    radius = floor(diameter/2)
    return diameter, radius

def determine_ring_location(square_num, diameter, radius):
    ''' Calculate the Index of a given Sqaure Number '''
    reference = (diameter - 2)**2 # Square number on the bottom right corner
    location_in_ring = abs(square_num - (reference+radius)) # Distance from Reference
    return location_in_ring

def main():
    ''' Calculate Steps '''

    square_num = 289326

    diameter, radius = create_circle(square_num) # To determine how far out we are
    ring_loc = determine_ring_location(square_num, diameter, radius)
    distance = radius + ring_loc
    print("Distance: %s" % distance)
    steps = radius + ring_loc % (diameter - 1)

    print('Steps: '+ str(steps))

if __name__ == '__main__':
    main()
