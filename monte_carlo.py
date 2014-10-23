__author__ = 'Timothy Rose-Innes'

class monte_carlo(object):

    def __init__(self, temp):
        self.temp = temp

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

        # Select particle at random
        nSelect = random_integers(n)

        #Count over particles up to n until reaching correct element
        count = 0
        i = -1

        while count < nSelect:
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
        # def compare_energies(self, density, density_new, energy):
        # if energy lower
        #   return true
        # else
        #   return false

    # Method Compare Boltzmann Factor
    # def compare_boltzmann_factor(self, density, density_new, energy):
    # Calculate Boltzmann factor P1 between E0 and E1
    # Compare to a random number P0 ??? What should the range be ???
    # if P0 > P1
	#   return true
    # else
    #   return false


# Method: Main (energy, density, iterations, temperature)
   # Create Monte Carlo Sim Object
   # Compute E0
   # Call move random
   # Compute E1
   # Call Compare Energies
   # Iterate