__author__ = 'Timothy Rose-Innes'

class monte_carlo(object):

    def __init__(self,temp):
        self.temp = temp

    # Randomly move a particle
    def random_move(self,density):
        # Count n particles
        #   Sum over all particles in density
        # Select particle at random
        #   Select random number 0 to n
        # Count over particles up to n until reach correct element
        # Subtract 1 from element
        # Add 1 to left/right element
        return density_new

    # Compare initial and final energies
    def compare_energies(self, density, density_new, energy):
        # if energy lower
        #   return true
        # else
        #   return false

    #Method Compare Boltzmann Factor
    def compare_boltzmann_factor(self, density, density_new, energy):
    # Calculate Boltzmann factor P1 between E0 and E1
    # Compare to a random number P0 ??? What should the range be ???
    # if P0 > P1
	#   return true
    # else
    #   return false


#Method: Main (energy, density, iterations, temperature)
   #Create Monte Carlo Sim Object
   #Compute E0
   #Call move random
   #Compute E1
   #Call Compare Energies
   #Iterate