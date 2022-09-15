def greedy_coin(change)
    """Return a dictionary with the coin type as the key and the number of coins as the value"""
  
    puts "Your change for #{change}:"
    coins = [0.25, 0.10, 0.05, 0.01]
    coin_lookup = {0.25 => "quarter", 0.10 => "dime", 0.05 => "nickel", 0.01 => "penny"}
    coin_dict = {}
    coins.each do |coin|
      coin_dict[coin] = 0
    end
    coins.each do |coin|
      while change >= coin
        change -= coin
        coin_dict[coin] += 1
      end
    end
    coin_dict.each do |coin|
      if coin[1] > 0
        puts "#{coin[1]} #{coin_lookup[coin[0]]}"
      end
    end
    return coin_dict
  end

greedy_coin(0.99)