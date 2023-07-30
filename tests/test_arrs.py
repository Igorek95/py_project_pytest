from utils import arrs


def test_get(array_fixture):
    assert arrs.get(array_fixture, 1, "test") == 2
    assert arrs.get(array_fixture, -1, "test") == "test"


def test_slice(array_fixture):
    assert arrs.my_slice(array_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(array_fixture, 1) == [2, 3, 4, 5]
    assert arrs.my_slice(array_fixture, -2) == [4, 5]
    assert arrs.my_slice(array_fixture, -8, 3) == [1, 2, 3]


def test_slice_empty_array(empty_array_fixture):
    assert arrs.my_slice(empty_array_fixture, 1) == []from utils import arrs


def test_get():
    assert arrs.get([1, 2, 3], 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"


def test_slice():
    assert arrs.my_slice([1, 2, 3, 4], 1, 3) == [2, 3]
    assert arrs.my_slice([1, 2, 3], 1) == [2, 3]
    assert arrs.my_slice([], 0) == []
    assert arrs.my_slice([1, 2, 3, 4], -5) == [1, 2, 3, 4]
    assert arrs.my_slice([1, 2, 3, 4], -1) == [4]
