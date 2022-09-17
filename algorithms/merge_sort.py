#!/usr/bin/env python

"""Merge Sort Algorithm in Python

Still needs work, not robust enough to handle all cases and long strings
Python sorted is more complete and robust than this.  Danger... Danger Will Robinson

"""

import random
import string
import click

# create a random string of characters
def random_string(length=4):
    """Generate a random string of characters"""

    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_pairs(text):
    """Create pairs of characters from a string"""

    print(f"Parsing unsorted string: {text}")
    pairs = []
    for i in range(0, len(text), 2):
        pairs.append(text[i : i + 2])
    return pairs


def sort_pair(pair):
    """Sort a pair of characters"""

    print(f"Sorting pair: {pair}")
    if pair[0] > pair[1]:
        new_pair = pair[1] + pair[0]
    else:
        new_pair = pair
    print(f"Sorted pair: {new_pair}")
    return new_pair


def sort_groups(pairs):
    """Sort lists of pairs into list"""

    print(f"Sorting pairs: {pairs}")
    current_pairs = []
    for pair in pairs:
        # first sort the pair
        sorted_pair = sort_pair(pair)
        if len(current_pairs) < 1:
            current_pairs.append(sorted_pair)
            print(f"Current pairs: {current_pairs}")
            continue
        elif len(current_pairs) == 1:
            current_pairs.append(sorted_pair)
            print(f"Current pairs: {current_pairs} length2")
            first_item = current_pairs[0][0]
            second_item = current_pairs[1][0]
            if first_item < second_item:
                continue
            else:
                # swap positions if first item is greater than second item
                current_pairs = [current_pairs[1], current_pairs[0]]
    return "".join(current_pairs)


# Create a function that process lists of pairs two at a time
def merge_sort(text=None, chunks=2, length=4):
    """Merge sort a string of characters in N chunks"""

    if text is None:
        text = random_string(length)
    rtext = text
    print(f"Processing Unsorted string: {rtext}")
    pairs = create_pairs(rtext)
    total = []
    for i in range(0, len(pairs), chunks):
        print(f"Processing pairs: {pairs[i:i+chunks]}")
        sorted_pairs = sort_groups(pairs[i : i + chunks])
        total.append(sorted_pairs)
    # return the sorted pairs
    return "".join(total)


@click.command()
@click.option("--length", default=4, help="Length of string to sort")
@click.option("--chunks", default=2, help="Number of chunks to sort")
@click.option("--text", default=None, help="Text to sort")
def main(text, chunks, length):
    """Merge sort a string of characters in N chunks"""

    print(merge_sort(text, chunks, length))


if __name__ == "__main__":
    # pylint: disable=no-value-for-parameter
    main()
