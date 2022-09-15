func greedy_coin(_ change: Double) -> [Double: Int] {
    print("Your change for \(change): ")
    let coins = [0.25, 0.10, 0.05, 0.01]
    let coin_lookup = [0.25: "quarter", 0.10: "dime", 0.05: "nickel", 0.01: "penny"]
    var coin_dict = [Double: Int]()
    for coin in coins {
        coin_dict[coin] = 0
    }
    for coin in coins {
        while change >= coin {
            change -= coin
            coin_dict[coin]! += 1
        }
    }
    for coin in coin_dict {
        if coin_dict[coin.key]! > 0 {
            print("\(coin_dict[coin.key]!) \(coin_lookup[coin.key]!)")
        }
    }
    return coin_dict
}