import pytest
from sorting import merge_sort

def test_merge_sort():
    assert merge_sort([3, 1, 2]) == [1, 2, 3]
    assert merge_sort([]) == []