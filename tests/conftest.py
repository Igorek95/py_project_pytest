import pytest

empty_array = []
array = [1, 2, 3, 4, 5]
empty_dict = {}

@pytest.fixture()
def array_fixture():
    return array


@pytest.fixture()
def empty_array_fixture():
    return empty_array


@pytest.fixture()
def dict_fixture():
    return empty_dict
