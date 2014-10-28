""" Unit tests for a diffusion model """
from nose.tools import assert_raises, assert_almost_equal
from diffusion_model import energy

def test_energy_fails_for_non_integer_density():
    with assert_raises(TypeError) as exception: energy([1.1, 2, 3])

def test_energy_fails_negative_density():
    with assert_raises(ValueError) as exception: energy([-1, 2, 3])

def test_energy_fails_density_wrong_dimension():
    with assert_raises(ValueError) as exception: energy([[1, 2], [3, 4]])

def test_zero_density():
    densities = [[], [0], [0, 0, 0]]
    for density in densities: assert_almost_equal(energy(density), 0)

def test_zero_coeff():
    assert_almost_equal(energy([1, 1, 1], coeff=0), 0)