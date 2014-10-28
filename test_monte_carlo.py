from monte_carlo import MonteCarlo
from nose.tools import assert_equal, assert_raises, assert_true, assert_false
from numpy.random import random_integers

#random_move tests

def test_fails_for_negative_densities():
    mc = MonteCarlo()
    with assert_raises(ValueError) as exception: mc.random_move([-1, 2, 3, 4])

def test_fails_for_non_integer_densities():
    mc = MonteCarlo()
    with assert_raises(ValueError) as exception: mc.random_move([1.0, 2, 3, 4])

def test_handles_zero_densities():
    mc = MonteCarlo()
    densities = [[],[0],[0,0,0,0]]
    for density in densities:
       with assert_raises(ValueError) as exception: mc.random_move(density)

def test_particle_number_is_conserved():
    mc = MonteCarlo()
    density = random_integers(100, size=100)
    n = sum(density)
    n_new = sum(mc.random_move(density))
    assert_equal(n,n_new,"particle number not consevered")

# TODO review test_one_particle_is_moved
# def test_one_particle_is_moved():
#     mc = MonteCarlo()
#     density = random_integers(100, size=10)
#     density_new = mc.random_move(density)
#     difference = density - density_new
#     print difference

# compare_energy tests

def test_compare_energies():
    mc = MonteCarlo()
    assert_true(mc.compare_energy(2,1))
    assert_false(mc.compare_energy(1,2))
    assert_false(mc.compare_energy(1,1))

# compare_boltzmann_factor tests

def test_compare_boltzman_factor_equal():
    mc = MonteCarlo()
    assert_true(mc.compare_boltzmann_factor(1,1))

def test_compare_boltzman_factor_high_t():
    mc = MonteCarlo(10000000000)
    assert_true(mc.compare_boltzmann_factor(100,1))

#TODO main algorithm tests