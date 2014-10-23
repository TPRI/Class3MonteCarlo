from monte_carlo import monte_carlo
from nose.tools import assert_equal, assert_raises

def test_fails_for_negative_densities():
    mc = monte_carlo(1)
    with assert_raises(ValueError) as exception: mc.random_move([-1, 2, 3])
