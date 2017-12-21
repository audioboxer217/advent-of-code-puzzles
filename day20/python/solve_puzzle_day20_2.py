''' Particle Swarm '''

import re
import numpy as np

REGEX = re.compile(r'([pva]=<)([^>]*)(>)')

def create_particle_dict(particles):
    ''' Create a dictionary of all particles '''

    particle_dict = {'particles': []}

    for particle in particles:
        part_details = particle.split(', ')
        positions = REGEX.match(part_details[0]).group(2).split(',')
        positions = list(map(int, positions))
        velocities = REGEX.match(part_details[1]).group(2).split(',')
        velocities = list(map(int, velocities))
        accelerations = REGEX.match(part_details[2]).group(2).split(',')
        accelerations = list(map(int, accelerations))
        temp_dict = {'pos': positions, 'vel': velocities, 'acc': accelerations}
        particle_dict['particles'].append(temp_dict)

    return particle_dict

def move_particles(dictionary):
    ''' Move the particles within the dictionary '''

    for i in range(len(dictionary['particles'])):
        part_pos = dictionary['particles'][i]['pos']
        part_vel = dictionary['particles'][i]['vel']
        part_acc = dictionary['particles'][i]['acc']

        part_vel[0] += part_acc[0]
        part_vel[1] += part_acc[1]
        part_vel[2] += part_acc[2]
        part_pos[0] += part_vel[0]
        part_pos[1] += part_vel[1]
        part_pos[2] += part_vel[2]

    return dictionary

def check_for_collision(dictionary):
    ''' Check for any collisions '''

    positions = []

    for i in range(len(dictionary['particles'])):
        part_pos = ''.join(str(dictionary['particles'][i]['pos']))
        positions.append(part_pos)

    positions_np = np.array(positions)

    remove = []
    for particle in positions:
        if positions.count(particle) > 1:
            matches = np.where(positions_np == particle)[0].tolist()
            remove += matches

    if remove:
        remove = np.unique(remove).tolist()
        for i in sorted(remove, reverse=True):
            del dictionary['particles'][i]

    return dictionary

def main():
    ''' Particle Swarm '''

    file = open('../puzzle_input.txt').read().split('\n')

    dictionary = create_particle_dict(file)

    for _ in range(10000):
        dictionary = move_particles(dictionary)
        dictionary = check_for_collision(dictionary)

    print(len(dictionary['particles']))

if __name__ == '__main__':
    main()
    