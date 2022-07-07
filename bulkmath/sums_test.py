import bulkmath
import pytest

@pytest.mark.parametrize("x, y, output",[(1,3,4), (5,5,10)])
def test_more_sums(x, y, output):
    assert bulkmath.sum(x,y) == output


def test_sum():
    assert bulkmath.sum(1,2) == 3

def test_tuples():
    assert bulkmath.map_sum_tuples([(1,3), (5,7)]) == [ 4, 12]