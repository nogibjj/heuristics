#!/usr/env/bin python
"""
A poker hand simulator
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
    #print the hands as well as the rank and type of hand
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
def info():
    """
    Displays all possible winning hands with examples
    """

    poker_hand_rank = display_poker_hand()
    poker_hand = build_poker_hand()
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

#build a play function that takes a bet
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
    #print the winner and the amount of money won or lost
    if status["winner"] == "Hand 1" and hand == 1:
        click.secho(f"{name} wins ${bet}! with Hand1", fg="green")
    elif status["winner"] == "Hand 2":
        click.secho(f"{name} loses ${bet}! with Hand2", fg="red")
    elif status["winner"] == "Tie":
        click.secho(f"It's a tie!", fg="yellow")

if __name__ == "__main__":
    cli()
