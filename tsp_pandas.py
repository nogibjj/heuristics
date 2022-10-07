import numpy as np
import random
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)
import pandas as pd


def create_cities():
    df = pd.DataFrame(
        {
            "city": [
                "New York",
                "Los Angeles",
                "Chicago",
                "Houston",
                "Philadelphia",
                "Phoenix",
                "San Antonio",
                "San Diego",
                "Dallas",
                "San Jose",
            ],
            "latitude": [
                40.7128,
                34.0522,
                41.8781,
                29.7604,
                39.9526,
                33.4484,
                29.4241,
                32.7157,
                32.7767,
                37.3382,
            ],
            "longitude": [
                -74.006,
                -118.2437,
                -87.6298,
                -95.3698,
                -75.1652,
                -112.0740,
                -98.4936,
                -117.1611,
                -96.7970,
                -121.8863,
            ],
        }
    )
    return df


def tsp_pandas(df):
    # create a new dataframe that will hold the shortest path
    df_shortest = pd.DataFrame(columns=["city", "latitude", "longitude"])
    # randomly select a starting city
    start_city = random.choice(df["city"])
    # add the starting city to the shortest path dataframe
    df_shortest = df_shortest.append(df[df["city"] == start_city])
    # remove the starting city from the original dataframe
    df = df[df["city"] != start_city]
    # loop through the original dataframe until it is empty
    while not df.empty:
        # create a list of distances from the last city in the shortest path to each city in the original dataframe
        distances = []
        for index, row in df.iterrows():
            distance = np.sqrt(
                (row["latitude"] - df_shortest.iloc[-1]["latitude"]) ** 2
                + (row["longitude"] - df_shortest.iloc[-1]["longitude"]) ** 2
            )
            distances.append(distance)
        # find the index of the city in the original dataframe that is closest to the last city in the shortest path
        closest_city_index = distances.index(min(distances))
        # add the closest city to the shortest path dataframe
        df_shortest = df_shortest.append(df.iloc[closest_city_index])
        # remove the closest city from the original dataframe
        df = df.drop(df.index[closest_city_index])
    # calculate the total distance of the shortest path
    total_distance = 0
    for index, row in df_shortest.iterrows():
        if index == 0:
            continue
        distance = np.sqrt(
            (row["latitude"] - df_shortest.iloc[index - 1]["latitude"]) ** 2
            + (row["longitude"] - df_shortest.iloc[index - 1]["longitude"]) ** 2
        )
        total_distance += distance
    # return the shortest path dataframe and the total distance
    return df_shortest, total_distance


def main():
    df = create_cities()
    min_distance = 100000000
    for _ in range(100):
        df_shortest, total_distance = tsp_pandas(df)
        if total_distance < min_distance:
            min_distance = total_distance
            min_df = df_shortest
    print(min_df)
    print(min_distance)


# call main
if __name__ == "__main__":
    main()
