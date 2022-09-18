#!/usr/env/bin python
"""
A poker hand simulator

Future updates:

- Add a web version
- add granularity to the simulation to allow for hands of same type to be ranked:  
i.e. 2 pair of 10s and 2 pair of 9s.  Currently, the simulator will only rank the
highest pair in each hand.

"""

import random
import click


def deck_of_cards():
    """
    Create a deck of cards
    """
    suits = ["H", "D", "C", "S"]
    ranks = [str(i) for i in range(2, 11)] + ["J", "Q", "K", "A"]
    deck = []
    for suit in suits:
        for rank in ranks:
            deck.append(rank + suit)
    return deck


def full_name_suit(suit):
    """
    Return the full name of the suit
    """
    if suit == "H":
        return "Hearts"
    elif suit == "D":
        return "Diamonds"
    elif suit == "C":
        return "Clubs"
    elif suit == "S":
        return "Spades"
    else:
        return "Unknown"


def deal_hand(deck, n=5):
    """
    Deal a hand of cards
    """
    return random.sample(deck, n)


def display_poker_hand():
    """Returns all possible poker hands with rank"""

    poker_hand_rank = {
        "Royal Flush": 10,
        "Straight Flush": 9,
        "Four of a Kind": 8,
        "Full House": 7,
        "Flush": 6,
        "Straight": 5,
        "Three of a Kind": 4,
        "Two Pair": 3,
        "One Pair": 2,
        "High Card": 1,
    }
    return poker_hand_rank


# build an example poker hand of all types of hands
def build_poker_hand():
    """
    Build all example poker hands
    """
    poker_hand = {
        "Royal Flush": ["10H", "JH", "QH", "KH", "AH"],
        "Straight Flush": ["9H", "10H", "JH", "QH", "KH"],
        "Four of a Kind": ["10H", "10D", "10C", "10S", "AH"],
        "Full House": ["10H", "10D", "10C", "AH", "AD"],
        "Flush": ["10H", "JH", "QH", "KH", "2H"],
        "Straight": ["9H", "10D", "JC", "QH", "KH"],
        "Three of a Kind": ["10H", "10D", "10C", "KH", "AH"],
        "Two Pair": ["10H", "10D", "JC", "JH", "KH"],
        "One Pair": ["10H", "10D", "JC", "QH", "KH"],
        "High Card": ["10H", "JD", "JC", "QH", "KH"],
    }
    return poker_hand


# build function that displays the probability of each hand of poker
def display_poker_hand_probability():
    """
    Display the probability of each hand of poker
    """
    poker_hand_probability = {
        "Royal Flush": 0.000154,
        "Straight Flush": 0.00139,
        "Four of a Kind": 0.0240,
        "Full House": 0.140,
        "Flush": 0.196,
        "Straight": 0.39,
        "Three of a Kind": 2.11,
        "Two Pair": 4.75,
        "One Pair": 42.2,
        "High Card": 50.1,
    }
    return poker_hand_probability


def evaluate_poker_hand(hand):
    """
    Evaluate a poker hand
    """
    # sort the hand
    hand = sorted(hand)
    # check for a flush
    if len(set([card[-1] for card in hand])) == 1:
        # check for a straight
        if len(set([card[:-1] for card in hand])) == 5:
            # check for a royal flush
            if hand[0][:-1] == "10" and hand[-1][:-1] == "A":
                return "Royal Flush"
            else:
                return "Straight Flush"
        else:
            return "Flush"
    # check for a straight
    elif len(set([card[:-1] for card in hand])) == 5:
        return "Straight"
    # check for a four of a kind
    elif len(set([card[:-1] for card in hand])) == 2:
        if len(set([card[:-1] for card in hand if card[:-1] == hand[0][:-1]])) == 1:
            return "Four of a Kind"
        else:
            return "Full House"
    # check for a three of a kind
    elif len(set([card[:-1] for card in hand])) == 3:
        if len(set([card[:-1] for card in hand if card[:-1] == hand[0][:-1]])) == 1:
            return "Three of a Kind"
        else:
            return "Two Pair"
    # check for a pair
    elif len(set([card[:-1] for card in hand])) == 4:
        return "One Pair"
    else:
        return "High Card"


def simulate_hands(deck, hands):
    """
    Simulate multiple hands of cards
    """
    results = []
    for _ in range(hands):
        results.append(deal_hand(deck))
    return results


# build a function to play two hands against each other
def play_poker_hand(hand1, hand2):
    """
    Play two poker hands against each other
    """

    hand1_rank = evaluate_poker_hand(hand1)
    hand2_rank = evaluate_poker_hand(hand2)
    hand1_rank_value = display_poker_hand()[hand1_rank]
    hand2_rank_value = display_poker_hand()[hand2_rank]
    # print the hands as well as the rank and type of hand
    print("Hand 1: {} - {} - {}".format(hand1, hand1_rank, hand1_rank_value))
    print("Hand 2: {} - {} - {}".format(hand2, hand2_rank, hand2_rank_value))
    # determine the winner
    if hand1_rank_value > hand2_rank_value:
        return {"winner": "Hand 1", "hand": hand1}
    elif hand1_rank_value < hand2_rank_value:
        return {"winner": "Hand 2", "hand": hand2}
    else:
        return {"winner": "Tie", "hand": hand1}


@click.group()
def cli():
    """
    A poker hand simulator
    """


@cli.command("info")
@click.option(
    "--probability", is_flag=True, help="Display the probability of each hand of poker"
)
def info(probability):
    """
    Displays all possible winning hands with examples
    """

    poker_hand_rank = display_poker_hand()
    poker_hand = build_poker_hand()
    if probability:
        poker_hand_probability = display_poker_hand_probability()
        for hand, _ in poker_hand_rank.items():
            # print probability of each hand with click colors and example and 1 in x chance
            click.secho(
                "{} - {} - 1 in {:,} - {:4f}%".format(
                    hand,
                    poker_hand[hand],
                    1 / poker_hand_probability[hand],
                    poker_hand_probability[hand],
                ),
                fg="yellow",
            )
    else:
        for hand in poker_hand_rank:
            click.secho(f"{hand}: ({poker_hand_rank[hand]})", fg="green")
            click.secho(f"{poker_hand[hand]}", fg="white")


@cli.command("deal")
@click.option("--hands", default=1, help="Number of hands to simulate")
def deal(hands):
    """
    Deal a hand of cards
    """
    deck = deck_of_cards()
    results = simulate_hands(deck, hands)
    for hand in results:
        # color the cards using click style
        for card in hand:
            if card[-1] in ["H", "D"]:
                click.secho(f"{card} ", fg="red", nl=False)
            else:
                click.secho(f"{card} ", fg="black", nl=False)
        click.echo()
        # print the hand rank
        hand_rank = evaluate_poker_hand(hand)
        click.echo(f"Hand Rank: {hand_rank}")


# build a play function that takes a bet
@cli.command("play")
@click.option("name", "--name", default="Player", help="Name of the player")
@click.option("hand", "--hand", default=1, help="Hand to play")
@click.option("--bet", default=1, help="Amount of money to bet")
def play(bet, name, hand):
    """
    Play a hand of poker against the computer with a bet
    """

    deck = deck_of_cards()
    hand1 = deal_hand(deck)
    hand2 = deal_hand(deck)
    status = play_poker_hand(hand1, hand2)
    # print the winner and the amount of money won or lost
    if status["winner"] == "Hand 1" and hand == 1:
        click.secho(f"{name} wins ${bet}! with Hand1", fg="green")
    elif status["winner"] == "Hand 2":
        click.secho(f"{name} loses ${bet}! with Hand2", fg="red")
    elif status["winner"] == "Tie":
        click.secho("It's a tie!", fg="yellow")


# build an interactive play function that takes a bet
@cli.command("interactive")
@click.option("name", "--name", default="Player", help="Name of the player")
@click.option("rounds", "--rounds", default=1, help="Number of rounds to play")
@click.option("money", "--money", default=100, help="Amount of money to start with")
def interactive(name, rounds, money):
    """
    Play a hand of poker against the computer with a bet
    """
    bet = 0
    history = {
        "rounds": 0,
        "expected_value": {},
        "probability_of_hand": {},
        "bet": {},
        "wins": 0,
        "losses": 0,
        "ties": 0,
        "money": money,
    }

    for i in range(1, rounds + 1):
        print(f"Round {i}:  Money: ${history['money']}")
        deck = deck_of_cards()
        hand1 = deal_hand(deck)
        hand2 = deal_hand(deck)
        hand_probability = display_poker_hand_probability()[evaluate_poker_hand(hand1)]
        print("Hand 1: {} - {}".format(hand1, evaluate_poker_hand(hand1)))
        # print probability of hand1 rounded to 2 decimal places
        print("Probability of Hand 1: {:.2f}%".format(hand_probability))
        # ask user how much they want to bet
        bet = click.prompt("How much would you like to bet?", type=int)
        status = play_poker_hand(hand1, hand2)
        history["probability_of_hand"][f"round{i}"] = hand_probability
        expected_value = (1 - (hand_probability * 0.01)) * abs(bet)
        history["expected_value"][f"round{i}"] = expected_value
        history["bet"][f"round{i}"] = bet
        # print the winner and the amount of money won or lost
        if status["winner"] == "Hand 1":
            click.secho(f"{name} wins ${bet}! with Hand1", fg="green")
        elif status["winner"] == "Hand 2":
            click.secho(f"{name} loses ${bet}! with Hand2", fg="red")
            bet = bet * -1
        elif status["winner"] == "Tie":
            bet = 0
            click.secho("It's a tie!", fg="yellow")

        # update the history
        history["rounds"] += 1
        history["money"] += bet
        if status["winner"] == "Hand 1":
            history["wins"] += 1
        elif status["winner"] == "Hand 2":
            history["losses"] += 1
        elif status["winner"] == "Tie":
            history["ties"] += 1
    # print the history
    click.secho(f"Rounds: {history['rounds']}", fg="green")
    click.secho(f"Wins: {history['wins']}", fg="green")
    click.secho(f"Losses: {history['losses']}", fg="red")
    click.secho(f"Ties: {history['ties']}", fg="yellow")
    click.secho(f"Money: {history['money']}", fg="green")
    click.secho(f"Expected Value: {history['expected_value']}", fg="green")
    click.secho(f"Probability of Hand: {history['probability_of_hand']}", fg="green")
    click.secho(f"Bets: {history['bet']}", fg="green")
    # sum of expected value vs money
    expected_value = sum(history["expected_value"].values())
    click.secho(
        f"Expected Value Total: {expected_value} vs Money {history['money']}", fg="red"
    )


if __name__ == "__main__":
    cli()
