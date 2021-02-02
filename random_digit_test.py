import pytest
import random

@pytest.mark.random
def test_random_with_N_digits():
    print("Random digits: {:06d}".format(random.SystemRandom().randint(0,999999)))
    print("{:02d}".format(7))




