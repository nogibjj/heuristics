import geopy
import geopy.distance
import pandas as pd
from random import shuffle


def create_cities_dataframe():
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


# run the similation 100 times and minimize for the shortest distance and print all cities visited
def main():
    # create a list to hold the distances
    distance_list = []
    # create a list to hold the city lists
    city_list_list = []
    # loop through the simulation 100 times
    cdf = create_cities_dataframe()
    for i in range(10):
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


# run the main function
if __name__ == "__main__":
    main()
