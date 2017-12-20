''' Particle Swarm '''

import re

REGEX = re.compile(r'([pva]=<)([^>]*)(>)')

def main():
    ''' Particle Swarm '''

    particles = open('../puzzle_input.txt').read().split('\n')

    particle_distances = []
    for particle in particles:
        part_details = particle.split(', ')
        positions = REGEX.match(part_details[0]).group(2).split(',')
        velocities = REGEX.match(part_details[1]).group(2).split(',')
        accelerations = REGEX.match(part_details[2]).group(2).split(',')
        pos_x = int(positions[0])
        pos_y = int(positions[1])
        pos_z = int(positions[2])
        vel_x = int(velocities[0])
        vel_y = int(velocities[1])
        vel_z = int(velocities[2])
        acc_x = int(accelerations[0])
        acc_y = int(accelerations[1])
        acc_z = int(accelerations[2])

        for _ in range(1000):
            vel_x += acc_x
            vel_y += acc_y
            vel_z += acc_z
            pos_x += vel_x
            pos_y += vel_y
            pos_z += vel_z

        particle_distances.append(abs(pos_x) + abs(pos_y) + abs(pos_z))

    closest = min(particle_distances)
    print(particle_distances.index(closest))

if __name__ == '__main__':
    main()
    