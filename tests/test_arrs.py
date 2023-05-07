from utils import arrs
import pytest


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get([1, 2, 3], 3, "test") == "test"
    assert arrs.get([1, 2, 3], -2, "test") == "test"


@pytest.fixture
def coll():
    return [1, 2, 3]
def test_slice(coll):
    assert arrs.my_slice(coll, 1, 3) == [2, 3]
    assert arrs.my_slice(coll, 1) == [2, 3]
    assert arrs.my_slice(coll, -1, 3) == [3]
    assert arrs.my_slice(coll, -5, 3) == [1, 2, 3]


def test_slice_with_void(coll):
    assert arrs.my_slice([], 1, 5) == []
