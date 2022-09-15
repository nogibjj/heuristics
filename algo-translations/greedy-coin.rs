//BROKEN CODE:  NOT WORKING

use std::collections::HashMap;

fn greedy_coin(change: f32) -> HashMap<f32, i32> {
    let mut coin_dict: HashMap<f32, i32> = HashMap::new();
    let coins = [0.25, 0.10, 0.05, 0.01];
    let coin_lookup = [(0.25, "quarter"), (0.10, "dime"), (0.05, "nickel"), (0.01, "penny")];

    for coin in coins {
        coin_dict.insert(coin, 0);
    }
    for coin in coins {
        while change >= coin {
            change -= coin;
            *coin_dict.get_mut(&coin).unwrap() += 1;
        }
    }
    for (coin, count) in coin_dict {
        if count > 0 {
            println!("{} {}", count, coin_lookup[coin]);
        }
    }
    coin_dict
}

fn main() {
    let change = 0.99;
    let coin_dict = greedy_coin(change);
}