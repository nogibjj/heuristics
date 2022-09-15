# build a greedy algorithm to find the minimum number of coins
def main():
    # get change amount from user
    while True:
        change = float(input("Change owed: "))
        if change > 0:
            break
    # convert change to cents
    cents = round(change * 100)
    # initialize coin count
    coins = 0
    # greedy algorithm
    while cents >= 25:
        cents -= 25
        coins += 1
    while cents >= 10:
        cents -= 10
        coins += 1
    while cents >= 5:
        cents -= 5
        coins += 1
    while cents >= 1:
        cents -= 1
        coins += 1
    # print result
    print(coins)

""" Here is the explanation of the greedy algorithm:
1. Start with the largest coin value and try to subtract it from the change amount as many times as possible.
2. If the change amount is less than the coin value, move on to the next smallest coin value.
3. Repeat until the change amount is 0.
4. The total number of coins used is the minimum number of coins required to make change.
5. If the change amount is negative, the coin value is too large and should be skipped.
6. If the change amount is positive, the coin value is too small and should be used.
7. If the change amount is 0, the minimum number of coins has been found.
8. The greedy algorithm does not always find the minimum number of coins, but it is fast and simple.

"""



if __name__ == "__main__":
    main()
