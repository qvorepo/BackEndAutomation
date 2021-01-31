import math_func
import pytest

@pytest.mark.parametrize('num1, num2, result',
                         [
                             (7,11,18),
                             (12,2,14),
                             (34.1, 2.9, 37),
                             ('Hello', ' World!', 'Hello World!')
                         ])
def test_add(num1, num2, result):
    assert math_func.add(num1, num2) == result



