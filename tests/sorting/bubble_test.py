import pytest
from sorting import bubble

@pytest.mark.parametrize("array", [
    [1,2,3,4,5,6],
    [6,7,8,9,1,3,4],
    [0,1],
    [1,0]
])
def test_bubble_sort(array):
    assert bubble.bubble_sort(array) == sorted(array)