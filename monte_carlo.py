__author__ = 'Timothy Rose-Innes'

class MonteCarlo(object):

    def __init__(self, temp=10, iterations=1000):

        #Check inputs

        if temp <= 0:
            raise ValueError("Temperature should be *positive*")

        if iterations <= 0:
            raise ValueError("Iterations should be *positive*")

        if type(iterations) != int:
            raise TypeError("Number of Iterations should be an *integer*.")

        self.temp = temp
        self.iterations = iterations

    # Randomly move a particle
    def random_move(self, density):

        # Imports
        from numpy import array, sum
        from numpy.random import random_integers
        import random

        # Assign density input to an array
        density = array(density)

        # Count n particles
        n = sum(density)

        if any(density < 0):
            raise ValueError("Density should be positive")

        if density.dtype != 'i':
            raise TypeError("Density should be an integer")

        if n == 0:
            raise ValueError("Densities should not be all zero")

        # Select particle at random
        n_select = random_integers(n)

        #Count over particles up to n until reaching correct element
        count = 0
        i = -1

        while count < n_select:
            i += 1
            count += density[i]

        #Subtract 1 from selected particle position
        density[i] -= 1

        #Add 1 particle to new position
        if i == 0:
            density[1] += 1
        elif i == len(density) - 1:
            density[i - 1] += 1
        else:
            density[(i + random.choice([-1, 1]))] += 1

        return density

    # Compare initial and final energies
    def compare_energy(self, en, en_new):

        if en_new < en:
            return True
        else:
            return False

    # Method Compare Boltzmann Factor
    def compare_boltzmann_factor(self, en, en_new):

        from numpy import exp
        from numpy.random import uniform

        boltz = exp(-(en_new - en)/self.temp)

        if boltz > uniform():
            return True
        else:
            return False

    def iteration(self, density, energy):

        en = energy(density)

        density_new = self.random_move(density)

        en_new = energy(density_new)

        if self.compare_energy(en, en_new):
            return [density_new, en_new]
        elif self.compare_boltzmann_factor(en, en_new):
            return [density_new, en_new]
        else:
            return [density, en]


    def __call__(self, density_initial, energy):

        #Imports
        from numpy import array

        # Check density_initial

        #Assign density list to an numpy array
        density_initial = array(density_initial)

        if density_initial.ndim != 1:
            raise ValueError("Density should be an a *1-dimensional* array.")

        if any(density_initial < 0):
            raise ValueError("Density should be an array of *positive integers*.")

        if density_initial.dtype.kind != 'i' and len(density_initial) > 0:
            raise TypeError("Density should be an array of *integers*.")

        i = 0

        density = density_initial

        while i < self.iterations:
            [density, en] = self.iteration(density, energy)
            i += 1
            #print [density, en, i]



