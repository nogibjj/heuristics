from algorithms.merge_sort import (
    random_string,
    create_pairs,
    sort_pair,
    sort_groups,
    merge_sort,
)
import pytest

# build a fixture to test the create_pairs function
@pytest.fixture
def ranstring():
    return "abzd"


@pytest.fixture
def list_pairs():
    return "ha"


# test each function in the merge_sort.py file
def test_random_string():
    """Test random_string function"""
    assert len(random_string(4)) == 4


def test_create_pairs(ranstring):
    """Test create_pairs function"""

    # assert len(create_pairs(ranstring)) == 2
    assert create_pairs(ranstring) == ["ab", "zd"]


def test_sort_pair(list_pairs):
    """Test sort_pair function"""
    assert sort_pair("ab") == "ab"
    assert sort_pair("ba") == "ab"
    assert sort_pair(list_pairs) == "ah"


def test_sort_groups():
    """Test sort_groups function"""
    assert sort_groups(["ca", "cd"]) == "accd"


def test_merge_sort():
    """Test merge sort"""

    assert merge_sort("ZENOVW").startswith("E")
    assert merge_sort("ZENOVW").endswith("W")
