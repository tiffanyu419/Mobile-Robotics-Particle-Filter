# E28 homework 9
#Tiffany Yu

import numpy as np
import matplotlib.pyplot as plt

# Given an array of particles (hypothetical positions) x, return
# the depth of each particle location in an array.
def depth_at(x):
    return 0.3 + ( 0.10 * np.cos(2.0*np.pi*(x - 0.03)) -
                   0.06 * np.cos(4.0*np.pi*(x - 0.52)) +
                   0.04 * np.cos(8.0*np.pi*(x + 0.88)) )

# Given an array of particles which may have left the [0,1) interval,
# "wrap" them back around into the interval using modular arithmetic.
def wrap_state(x):
    return x - np.floor(x)

# Sample from the motion model of the robot by taking an array of
# particles x and applying an additive offset u and random noise with
# the given standard deviation sigma_x.
def sample_motion(x, u, sigma_x):
    x = np.array(x)
    return wrap_state(x + u + np.random.normal(scale=sigma_x, size=x.shape))

# Given an array of particles x and an action u, return a new array that
# is the result of the motion step of the particle filter.
def motion_update(x, u, sigma_x):
    prior_bel = sample_motion(x, u, sigma_x)
    return prior_bel

# Given an array of particles x and a measurement z, return a new array
# that is the result of the measurement step of the particle filter.
def measurement_update(x, z, sigma_z):
    # TODO: compute weights for each particle
    w = np.exp(-np.power((z-depth_at(x)),2)/(2*np.power(sigma_z,2)))
    sum = w.sum()
    w /= sum
    
    # TODO: resample particles using weights by calling np.random.choice

    meas_step = np.random.choice(x,200,p = w)
    return meas_step

# Alternates motion and measurement models given control/measurement
# data, and plots nicely.
def run_particle_filter(num_particles, sigma_x, sigma_z, input_file):

    u_and_z = np.genfromtxt(input_file)

    particles = np.linspace(0, 1, num_particles, False)
    ystep = 0.5
    
    y = np.zeros_like(particles)

    plt.plot(particles, y, 'b.')

    for row in u_and_z:
        
        u, z = tuple(row)
        
        print ('running motion step with u={}'.format(u))
        particles = motion_update(particles, u, sigma_x)

        y += ystep
        plt.plot(particles, y, 'g.')

        print ('running measurement step with z={}'.format(z))
        particles = measurement_update(particles, z, sigma_z)

        y += ystep
        plt.plot(particles, y, 'b.')

    plt.xlabel('Particle location')
    plt.ylabel('Iteration')
    plt.title('Particle filter results')
    plt.show()

if __name__ == '__main__':

    run_particle_filter(200, 0.01, 0.03, 'assignment_data.txt')
