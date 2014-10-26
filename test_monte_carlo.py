from monte_carlo import monte_carlo
from nose.tools import assert_equal, assert_raises
from numpy.random import random_integers

def test_fails_for_negative_densities():
    mc = monte_carlo()
    with assert_raises(ValueError) as exception: mc.random_move([-1, 2, 3, 4])

def test_fails_for_non_integer_densities():
    mc = monte_carlo()
    with assert_raises(ValueError) as exception: mc.random_move([1.0, 2, 3, 4])

def test_handles_zero_densities():
    mc = monte_carlo()
    densities = [[],[0],[0,0,0,0]]
    for density in densities:
       with assert_raises(ValueError) as exception: mc.random_move(density)

def test_particle_number_is_conserved():
    mc = monte_carlo()
    density = random_integers(100, size=100)
    n = sum(density)
    n_new = sum(mc.random_move(density))
    assert_equal(n,n_new,"particle number not consevered")

# def one_particle_is_moved():
#     mc = monte_carlo()
#     density = random_integers(100, size=10)
#     density_new = mc.random_move(density)
#     difference = density - density_new
#     print difference


