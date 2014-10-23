from monte_carlo import random_move
from nose.tools import assert_equal, assert_raises

def test_fails_for_negative_densities():
    with assert_raises(ValueError) as exception: energy([-1, 2, 3]):
