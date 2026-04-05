import pytest
from sorting import quick_sort

def test_quick_sort():
    assert quick_sort([3, 1, 2]) == [1, 2, 3]
    assert quick_sort([5, 5, 5]) == [5, 5, 5]