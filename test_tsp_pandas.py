from pytest import fixture
from tsp_pandas import create_cities, tsp_pandas


@fixture
def cities():
    return create_cities()


def test_tsp_pandas(cities):
    df_shortest, total_distance = tsp_pandas(cities)
    assert total_distance < 100000000
