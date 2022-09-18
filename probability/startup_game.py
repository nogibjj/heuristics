#!/usr/bin/env python

import random
import click


def generate_true_false(probability=0.23, num=4):
    """Return True/False with probability

    Args:
        probability (floating point decimal): probability of True/False ex. [0.5, 0.5] or [0.023, 0.977]
        num (int): number of scenarios to generate

    """
    # print probability as a percentage with 2 decimal places and % sign using f-string
    print(f"Probability of True: {probability*100:.2f}%")
    scene_probability = [probability, 1 - probability]
    scenarios = [
        random.choices([True, False], scene_probability)[0] for _ in range(num)
    ]
    print("Startup SUCCESS: {}".format(scenarios.count(True)))
    print("Startup FAIL: {}".format(scenarios.count(False)))
    # print actual ratio of True/False formatted to 4 decimal places and percentage
    print("Ratio True/False: {:.4f}%".format(scenarios.count(True) / num * 100))
    return scenarios


# create function that accepts value of startup, percentage of company owned and a number of scenarios
def calculate_value(
    startup_valuation=100000000,
    percent_owned=0.01,
    simulations=4,
    probability=0.23,
):
    """Select the amount of startups worked for in a row
    Assumes 1 in 43 startups succeed
    Assumes 1% of company owned
    Assumes 100 million valuation
    Assumes 4 startups worked for in a row (about 16 years of career)
    """
    total = 0
    for simulation in range(1, simulations + 1):
        # generate scenarios with probability 0.5
        scenarios = generate_true_false(probability, simulations)
        # if True, add value of startup to total
        if scenarios[0]:
            total += startup_valuation * percent_owned
        # if False, subtract value of startup from total
        else:
            total -= 0
        # print total value of startup
        print(f"Cumulative Total value of startup: {total} Company #{simulation}")
    return total


# create function that uses calculate_value function to determine how many people earned money from startups and total
def calculate_value_multiple(
    startup_valuation=100000000,
    percent_owned=0.01,
    simulations=4,
    probability=0.23,
    people=1000,
):
    """Calculate the value of startup for multiple people

    Args:
        startup_valuation (int): value of startup
        percent_owned (float): percent of company owned
        simulations (int): number of startups worked for in a row
        probability (float): probability of startup success
        people (int): number of people to simulate

    Returns:
        int: total value of startup for all people
    """
    total = 0
    count_people_making_money = 0
    for person in range(1, people + 1):
        # calculate value of startup for each person
        if (
            calculate_value(startup_valuation, percent_owned, simulations, probability)
            > 0
        ):
            count_people_making_money += 1
        total += calculate_value(
            startup_valuation=startup_valuation,
            percent_owned=percent_owned,
            simulations=simulations,
            probability=probability,
        )
        print(f"Total value of startup for all people: {total} Person #{person}")
    # print average value of startup for all people
    print(f"Average value of startup for all people: {total/people}")
    # print how many people earned money from startup
    print(f"Number of people making money from startup: {count_people_making_money}")
    # print how many people making no money from startup
    print(
        f"Number of people making no money from startup: {people - count_people_making_money}"
    )
    # print percentage of people making money from startup
    print(
        f"Percentage of people making money from startup: {count_people_making_money/people*100:.2f}%"
    )

    return total


def simulate_investor(startup_valuation=100000000, simulations=100, probability=0.023):
    """Simulate a venture capitalist investing in a porfolio of companies"""
    total = 0
    amount_invested = 100000
    for simulation in range(1, simulations + 1):
        # generate scenarios with probability 0.5
        scenarios = generate_true_false(probability, simulations)
        # if True, add value of startup to total
        percentage_owned = random.uniform(0.25, 0.50)
        print(f"Percentage owned: {percentage_owned}")
        if scenarios[0]:
            total += startup_valuation * percentage_owned
        # if False, subtract value of startup from total
        else:
            total -= 0
        # print total value of startup
        print(f"Cumulative Total value of startup: {total} Company #{simulation}")
    return_on_investment = total / amount_invested*simulations
    return return_on_investment

def sanity_test(num):
    """Show the ratio of True/False is close to the probability via law or large numbers"""

    # generate 10 scenarios with probability 0.5
    generate_true_false([0.5, 0.5], num)
    # generate 10 scenarios with probability 0.023 (1 in 43 startups succeed)
    generate_true_false([0.023, 0.977], num)

@click.group()
def cli():
    """Startup Game Simulator"""


# add a command to the cli
@cli.command("sanity")
@click.option("--num", default=100, help="Number of scenarios to generate")
def sanity(num):
    """Sanity test the simulation with a small number of scenarios

    Example:
        python startup_game.py sanity --num 10
    """

    sanity_test(num=num)


@cli.command("vcportfolio")
@click.option("--startup_valuation", default=100000000, help="Value of startup")
@click.option("--simulations", default=100, help="Number of startups worked for in a row")
@click.option("--probability", default=0.023, help="Probability of startup success")
def vcportfolio(startup_valuation, simulations, probability):
    """Simulate a venture capitalist investing in a porfolio of companies

    Example:
        python startup_game.py vcportfolio --startup_valuation 100000000 --simulations 100 --probability 0.23
    """
    
    click.echo(click.style(f"Startup Valuation: {startup_valuation}", fg="green"))
    click.echo(click.style(f"Simulations (Companies in Portfolio): {simulations}", fg="green"))
    click.echo(click.style(f"Probability of success: {probability}", fg="green"))
    #show return on investment for venture capitalist
    click.echo(click.style(f"Return on Investment: {simulate_investor(startup_valuation, simulations, probability)}", fg="green"))

@cli.command("simulate")
@click.option("--startup_valuation", default=100000000, help="Value of startup")
@click.option("--percent_owned", default=0.01, help="Percent of company owned")
@click.option("--simulations", default=4, help="Number of startups worked for in a row")
@click.option("--probability", default=0.023, help="Probability of success")
def simulate(startup_valuation, percent_owned, simulations, probability):
    """Simulate a startup career

    Example:
        python startup_game.py simulate --startup_valuation 100000000 --percent_owned 0.01 --simulations 4 --probability 0.023
    """

    total = calculate_value(startup_valuation, percent_owned, simulations, probability)
    # use click colors to print total
    click.secho("Total: {}".format(total), fg="green")


# add a command to the cli
@cli.command("simulate_multiple")
@click.option("--startup_valuation", default=100000000, help="Value of startup")
@click.option("--percent_owned", default=0.01, help="Percent of company owned")
@click.option("--simulations", default=4, help="Number of startups worked for in a row")
@click.option("--probability", default=0.023, help="Probability of success")
@click.option("--people", default=1000, help="Number of people to simulate")
def simulate_multiple(
    startup_valuation, percent_owned, simulations, probability, people
):
    """Simulate a startup career for multiple people

    Example:
        python startup_game.py simulate_multiple --startup_valuation 100000000\
            --percent_owned 0.01 --simulations 4 --probability 0.023 --people 1000
    """

    total = calculate_value_multiple(
        startup_valuation, percent_owned, simulations, probability, people
    )
    # use click colors to print total
    click.secho("Total Earned: {}".format(total), fg="green")


# run the code
if __name__ == "__main__":
    cli()
