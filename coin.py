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


if __name__ == "__main__":
    main()
