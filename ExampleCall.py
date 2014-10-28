__author__ = 'Timothy Rose-Innes'

""" An example of calling an instance of the MonteCarlo class """

from monte_carlo import MonteCarlo
from diffusion_model import energy
from numpy.random import random_integers

# Create an instance, mc, of the MonteCarlo class
mc = MonteCarlo(1,1000)

# Call the instance mc 
mc(random_integers(100, size=10), energy)

