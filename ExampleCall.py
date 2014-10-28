__author__ = 'Timothy Rose-Innes'

from monte_carlo import MonteCarlo
from diffusion_model import energy
from numpy.random import random_integers

mc = MonteCarlo(1,1000)
mc(random_integers(100, size=10), energy)

