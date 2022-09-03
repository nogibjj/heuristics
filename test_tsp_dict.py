from tsp_dict import tsp
from pytest import fixture


@fixture
def cities():
    return {
        "New York": {
            "New York": 0,
            "Chicago": 800,
            "Denver": 1400,
            "Los Angeles": 2100,
        },
        "Chicago": {"New York": 800, "Chicago": 0, "Denver": 600, "Los Angeles": 1300},
        "Denver": {"New York": 1400, "Chicago": 600, "Denver": 0, "Los Angeles": 700},
        "Los Angeles": {
            "New York": 2100,
            "Chicago": 1300,
            "Denver": 700,
            "Los Angeles": 0,
        },
    }


def test_tsp(cities):
    assert tsp(cities), _ == 4000
