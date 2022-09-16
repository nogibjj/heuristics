from fetch_cities_lat_long import main, my_cities, create_cities_dataframe
import pytest

# create a list of cities
city_list = my_cities("New York", "Knoxville", "Los Angeles", "Chicago")
# create a dataframe of cities and their latitudes and longitudes
df = create_cities_dataframe(city_list)


@pytest.mark.slow
def test_my_cities():
    """Test my_cities function"""
    assert my_cities("New York", "Knoxville", "Los Angeles", "Chicago") == [
        "New York",
        "Knoxville",
        "Los Angeles",
        "Chicago",
    ]


@pytest.mark.slow
def test_main():
    """Test main function"""
    assert main(count=1) == None
