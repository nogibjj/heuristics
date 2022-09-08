#!/usr/bin/env python

"""
This is a command-line tool that figures out the shortest distance to visit all cities in a list.
"""


import geopy
import geopy.distance
import pandas as pd
from random import shuffle
import click

# build a function that takes variable length argument of strings and returns a list of cities
def my_cities(*args):
    """Build a list of cities from input"""
    return list(args)


def create_cities_dataframe(cities=None):
    """Create a Pandas DataFrame of cities and their latitudes and longitudes"""

    if cities is None:
        cities = [
            "New York",
            "Knoxville",
            "Birmingham",
            "Baltimore",
            "Bangor",
            "Cleveland",
            "Chicago",
            "Denver",
            "Los Angeles",
            "San Francisco",
            "Raleigh",
            "Seattle",
            "Boston",
            "Houston",
            "Dallas",
            "Miami",
            "Atlanta",
            "Fort Worth",
            "Phoenix",
            "San Diego",
        ]

    # create a list to hold the latitudes and longitudes
    latitudes = []
    longitudes = []
    # loop through the cities list and get the latitudes and longitudes
    for city in cities:
        geolocator = geopy.geocoders.Nominatim(user_agent="tsp_pandas")
        location = geolocator.geocode(city)
        latitudes.append(location.latitude)
        longitudes.append(location.longitude)
    # create a dataframe from the cities, latitudes, and longitudes
    df = pd.DataFrame(
        {
            "city": cities,
            "latitude": latitudes,
            "longitude": longitudes,
        }
    )
    return df


def tsp(cities_df):
    """Traveling Salesman Problem using Pandas and Geopy"""

    # create a list of cities
    city_list = cities_df["city"].to_list()
    # shuffle the list to randomize the order of the cities
    shuffle(city_list)
    print(f"Randomized city_list: {city_list}")
    # create a list of distances
    distance_list = []
    # loop through the list
    for i in range(len(city_list)):
        # if i is not the last item in the list
        if i != len(city_list) - 1:
            # get the distance between the current city and the next city
            distance = geopy.distance.distance(
                (
                    cities_df[cities_df["city"] == city_list[i]]["latitude"].values[0],
                    cities_df[cities_df["city"] == city_list[i]]["longitude"].values[0],
                ),
                (
                    cities_df[cities_df["city"] == city_list[i + 1]]["latitude"].values[
                        0
                    ],
                    cities_df[cities_df["city"] == city_list[i + 1]][
                        "longitude"
                    ].values[0],
                ),
            ).miles
            # append the distance to the distance list
            distance_list.append(distance)
        # if i is the last item in the list
        else:
            # get the distance between the current city and the first city
            distance = geopy.distance.distance(
                (
                    cities_df[cities_df["city"] == city_list[i]]["latitude"].values[0],
                    cities_df[cities_df["city"] == city_list[i]]["longitude"].values[0],
                ),
                (
                    cities_df[cities_df["city"] == city_list[0]]["latitude"].values[0],
                    cities_df[cities_df["city"] == city_list[0]]["longitude"].values[0],
                ),
            ).miles
            # append the distance to the distance list
            distance_list.append(distance)
    # return the sum of the distance list and the city list
    total_distance = sum(distance_list)
    return total_distance, city_list


def main(count, df=None):
    """Main function that runs the tsp similution multiple times"""
    # create a list to hold the distances
    distance_list = []
    # create a list to hold the city lists
    city_list_list = []
    # loop through the simulation
    if df is None:
        cdf = create_cities_dataframe()
    else:
        cdf = df
    for i in range(count):  # run the simulation x times
        # get the distance and city list
        distance, city_list = tsp(cdf)
        print(f"Running similation: {i}:  Found total distance: {distance}")
        # append the distance to the distance list
        distance_list.append(distance)
        # append the city list to the city list list
        city_list_list.append(city_list)
    # get the index of the shortest distance
    shortest_distance_index = distance_list.index(min(distance_list))
    # print the shortest distance
    print("Shortest Distance: {}".format(min(distance_list)))
    # print the cities visited
    print("Cities Visited: {}".format(city_list_list[shortest_distance_index]))


# create click group
@click.group()
def cli():
    """This is a command-line tool that figures out the shortest distance to visit all cities in a list."""


# create a click command that takes a variable number of arguments of cities passed in
@cli.command("cities")
@click.argument("cities", nargs=-1)
@click.option("--count", default=5, help="Number of simulations to run")
def cities_cli(cities, count):
    """This is a command-line tool that figures out the shortest distance to visit all cities in a list.

    Example: ./fetch_cities_lat_long.py cities "New York" "Knoxville" --count 2
    """

    # create a list of cities
    city_list = my_cities(*cities)
    # create a dataframe of cities and their latitudes and longitudes
    cities_df = create_cities_dataframe(city_list)
    # run the tsp function
    main(count, cities_df)


# add click command that runs the similation x times
@cli.command("simulate")
@click.option("--count", default=10, help="Number of times to run the simulation.")
def simulate(count):
    """Run the simulation x times and print the shortest distance and cities visited.

    Example:
        ./fetch_cities_lat_long.py simulate --count 15

    """

    print(f"Running simulation {count} times")
    main(count)


if __name__ == "__main__":
    cli()


# run the main function
if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
