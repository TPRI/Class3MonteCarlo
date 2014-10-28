__author__ = 'Timothy Rose-Innes'

class MonteCarlo(object):
    """ A Simple Monte Carlo Algorithm"""

    def __init__(self, temp=10, iterations=1000):

        # Check inputs
        if temp <= 0:
            raise ValueError("Temperature should be *positive*")

        if iterations <= 0:
            raise ValueError("Iterations should be *positive*")

        if type(iterations) != int:
            raise TypeError("Number of Iterations should be an *integer*.")

        self.temp = temp
        """ Temperature to run simulation """

        self.iterations = iterations
        """ Number of iterations """

    def random_move(self, density):
        """ Move a randomly selected particle left or right """

        # Imports
        from numpy import array, sum
        from numpy.random import random_integers
        import random

        # Assign density input to an array
        density = array(density)

        # Count n particles
        n = sum(density)

        # Check density
        if any(density < 0):
            raise ValueError("Density should be positive")

        if density.dtype != 'i':
            raise TypeError("Density should be an integer")

        if n == 0:
            raise ValueError("Densities should not be all zero")

        # Select particle at random
        n_select = random_integers(n)

        # Count over particles until the correct element is reached
        count = 0
        i = -1

        while count < n_select:
            i += 1
            count += density[i]

        # Subtract 1 from initial particle position
        density[i] -= 1

        # Add 1 particle to new position
        if i == 0:
            density[1] += 1
        elif i == len(density) - 1:
            density[i - 1] += 1
        else:
            density[(i + random.choice([-1, 1]))] += 1

        return density

    def compare_energy(self, en, en_new):
        """  Return True if the new energy is less than the initial energy """

        if en_new < en:
            return True
        else:
            return False

    def compare_boltzmann_factor(self, en, en_new):
        """  Compare Boltzmann factor against a uniform distribution """

        from numpy import exp
        from numpy.random import uniform

        # Boltzmann factor
        boltz = exp(-(en_new - en)/self.temp)

        # Compare against a uniform distribution
        if boltz > uniform():
            return True
        else:
            return False

    def iteration(self, density, energy):
        """ A single iteration of the Monte Carlo Algorithm """

        # Initial energy
        en = energy(density)

        # Randomly move a particle
        density_new = self.random_move(density)

        # The new energy
        en_new = energy(density_new)

        # Decide if to accept change
        if self.compare_energy(en, en_new):
            return [density_new, en_new]
        elif self.compare_boltzmann_factor(en, en_new):
            return [density_new, en_new]
        else:
            return [density, en]


    def __call__(self, density_initial, energy):
        """ Implements the main Monte Carlo Algorithm """

        from numpy import array

        #Assign density list to a numpy array
        density_initial = array(density_initial)

        # Check initial density
        if density_initial.ndim != 1:
            raise ValueError("Density should be an a *1-dimensional* array.")

        if any(density_initial < 0):
            raise ValueError("Density should be an array of *positive integers*.")

        if density_initial.dtype.kind != 'i' and len(density_initial) > 0:
            raise TypeError("Density should be an array of *integers*.")

        # Set iterator to 0
        i = 0

        density = density_initial

        # Loop through the iterations
        while i < self.iterations:
            [density, en] = self.iteration(density, energy)
            i += 1
            # print density
            # Can add output here



