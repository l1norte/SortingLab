import pytest
from sorting import merge_sort, quick_sort

@pytest.mark.parametrize("sort_func", [merge_sort, quick_sort])
def test_sorting_algorithms(sort_func):
    assert sort_func([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
    assert sort_func([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]
    assert sort_func([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]
    assert sort_func([]) == []
    assert sort_func([7, 7, 7, 7]) == [7, 7, 7, 7]