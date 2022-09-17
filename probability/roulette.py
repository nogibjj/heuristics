#!/usr/bin/env python
"""
Examples of routines for simulating a roulette wheel.
The big takeaway is the concept of the law of large numbers.
Roulette has a negative expected value, so you will lose money in the long run.

Future improvements:

    * Allow for bets on multiple numbers and colors as well as odd/even, etc
    * Allow for different bets on different spins
    * Jupyter notebook with interactive widgets to show historical results
    * Add a web interface to allow for bets and results using streamlit or gradio

"""
import pandas as pd
import click
import sys


def build_wheel():
    """
    Roulette wheel with 38 slots and probabilities of landing on each slot
    """

    wheel = pd.DataFrame(
        [
            [0, "green", 0],
            [1, "red", 1],
            [2, "black", 2],
            [3, "red", 3],
            [4, "black", 4],
            [5, "red", 5],
            [6, "black", 6],
            [7, "red", 7],
            [8, "black", 8],
            [9, "red", 9],
            [10, "black", 10],
            [11, "black", 11],
            [12, "red", 12],
            [13, "black", 13],
            [14, "red", 14],
            [15, "black", 15],
            [16, "red", 16],
            [17, "black", 17],
            [18, "red", 18],
            [19, "red", 19],
            [20, "black", 20],
            [21, "red", 21],
            [22, "black", 22],
            [23, "red", 23],
            [24, "black", 24],
            [25, "red", 25],
            [26, "black", 26],
            [27, "red", 27],
            [28, "black", 28],
            [29, "black", 29],
            [30, "red", 30],
            [31, "black", 31],
            [32, "red", 32],
            [33, "black", 33],
            [34, "red", 34],
            [35, "black", 35],
            [36, "red", 36],
            [37, "green", 0],
        ],
        columns=["slot", "color", "number"],
    )
    # add the probabilities of landing on each slot
    wheel["probability"] = [1 / 38] * 38
    return wheel


def spin_wheel(wheel):
    """
    Simulate a single spin of the roulette wheel
    """
    return wheel.sample(n=1, weights="probability")


def simulate_spins(wheel, spins):
    """
    Simulate multiple spins of the roulette wheel
    """
    results = []
    for _ in range(spins):
        results.append(spin_wheel(wheel))
    return pd.concat(results)


def generate_report(results, full_report=False):
    """
    Generate a report on the results of the roulette wheel simulation
    """
    print(f"Total number of spins: {len(results)}")
    if full_report:
        print(
            f"Number of times each number landed: {results['number'].value_counts()[results['number'].value_counts() > 1]}"
        )
    # only print the color
    print(f"Number of times each color landed:\n {results['color'].value_counts()}")


def calculate_winnings(results, bet, count, color=None, number=None):
    """
    Calculate the winnings of the roulette wheel simulation
    using bet amount and number of spins for each color or number bet
    """
    color_winnings = 0
    number_winnings = 0
    total_amount_bet = count * bet

    if color == "red":
        color_winnings = (
            results[results["color"] == "red"]["slot"].count() * (bet * 2)
            - total_amount_bet
        )
    elif color == "black":
        color_winnings = (
            results[results["color"] == "black"]["slot"].count() * (bet * 2)
            - total_amount_bet
        )
    elif color == "green":
        color_winnings = (
            results[results["color"] == "green"]["slot"].count() * (bet * 17)
            - total_amount_bet
        )

    if number:
        number_winnings = (
            results[results["number"] == number]["slot"].count() * (bet * 35)
            - total_amount_bet
        )
        ncount = results[results["number"] == number]["slot"].count()
        print(f"Total count for number bet on [{number}]: {ncount}")

    grand_total = sum([color_winnings, number_winnings])
    return grand_total


# build a function to print each run of the wheel with red and black colors using click style
def print_wheel(results):
    """
    Print the results of the roulette wheel simulation
    """
    for _, row in results.iterrows():
        if row["color"] == "red":
            click.secho(f"{row['slot']}", fg="red", nl=False)
        elif row["color"] == "black":
            click.secho(f"{row['slot']}", fg="black", nl=False)
        else:
            # if the number is 37 replace it with 00 and don't print number
            if row["slot"] == 37:
                click.secho("00", fg="green", nl=False)
            else:
                click.secho(f"{row['slot']}", fg="green", nl=False)
        click.echo(" ", nl=False)
    click.echo()


@click.group()
def cli():
    """
    A group of commands for simulating a roulette wheel
    """


@cli.command("spin")
@click.option("--count", default=1, help="Total count of spins")
@click.option(
    "--color", type=click.Choice(["red", "black", "green"]), help="Color to bet on"
)
@click.option("--bet", default=1, help="Amount to bet on each spin")
@click.option("--bet", default=1, help="Amount of money to bet")
@click.option(
    "--number_bet", default=None, help="Number to bet on", type=click.IntRange(0, 36)
)
def spin_option(count, bet, number_bet, color):
    """
    Spin the roulette wheel:

     Example:
        Ten spins of the wheel with a bet of $1 on red
        ./roulette.py spin --count 10 --color red --bet 1

    """
    print(f"Selected number of spins: {count}")
    if not number_bet and not color:
        print("No bet selected")
    else:
        print(f"Selected bet amount: {bet}")
    if number_bet and color:
        print("Can't bet on color and number at the same time")
        # exit the program if both color and number are selected
        sys.exit()

    print(f"Selected number to bet on: {number_bet}")
    print(f"Selected color to bet on: {color}")

    # build the wheel
    wheel = build_wheel()
    # simulate the spins
    results = simulate_spins(wheel, count)
    # print the results
    print_wheel(results)
    generate_report(results)
    # print the winnings
    total_winnings = calculate_winnings(
        results=results, bet=bet, count=count, color=color, number=number_bet
    )
    print(f"Total winnings: {total_winnings}")


# run the cli
if __name__ == "__main__":
    cli()
