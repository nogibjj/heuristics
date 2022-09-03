#!/usr/bin/env python

import random


def tsp(cities):
    # create a list of cities
    city_list = list(cities.keys())
    # shuffle the list
    random.shuffle(city_list)
    # create a list of distances
    distance_list = []
    # loop through the list
    for i in range(len(city_list)):
        # if i is not the last item in the list
        if i != len(city_list) - 1:
            # get the distance between the current city and the next city
            distance = cities[city_list[i]][city_list[i + 1]]
            # append the distance to the distance list
            distance_list.append(distance)
        # if i is the last item in the list
        else:
            # get the distance between the current city and the first city
            distance = cities[city_list[i]][city_list[0]]
            # append the distance to the distance list
            distance_list.append(distance)
    # return the sum of the distance list and the city list
    return sum(distance_list), city_list


# main function
def main():
    # create a dictionary of 10 American cities and their distances from each other
    cities = {
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

    # call the tsp function and unpack the return values
    distance, city_list = tsp(cities)
    # print the distance and city list
    print("The distance is {} and the city list is {}".format(distance, city_list))

    # call the tsp function
    return tsp(cities)


def run():
    # create a list of distances
    distance_list = []
    # create a list of city lists
    city_list = []
    # loop 100 times
    for _ in range(100):
        # call the main function
        distance, cities = main()
        # append the distance to the distance list
        distance_list.append(distance)
        # append the city list to the city list
        city_list.append(cities)
    # get the index of the minimum distance
    index = distance_list.index(min(distance_list))
    # print the minimum distance and the city list
    print(min(distance_list), city_list[index])


if __name__ == "__main__":
    run()
