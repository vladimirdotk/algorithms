import pytest
from sorting import bubble, insertion


@pytest.mark.parametrize("array", [
    [1, 2, 3, 4, 5, 6],
    [6, 7, 8, 9, 1, 3, 4],
    [0, 1],
    [1, 0]
])
class TestSorting:

    def test_bubble_sort(self, array):
        assert bubble.sort(array) == sorted(array)

    def test_insertion_sort(self, array):
        assert insertion.sort(array) == sorted(array)
