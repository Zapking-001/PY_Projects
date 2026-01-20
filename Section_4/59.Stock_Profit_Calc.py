"""
Docstring for 59.Stock_Profit_Calc: 
    LOGIC of How it works:
      Instead of comparing every possible pair of days (which is slow), we imagine walking through time. 
      We keep track of the "cheapest" price we've seen so far and check if selling "today" at the current price,
      It would give us a better profit than what we've recorded previously
    
    Ex: If user inputs -> [10, 7, 5, 8, 11, 9]
        Expected Output: 6 (Buying at 5 and selling at 11).


            Efficiency : Time complexity: O(n)
                         Space complexity: O(1)

"""

# Method - 1
def stock_profit_efficient():
    data = input("Enter daily stock prices (space separated): ")
    prices = [float(x) for x in data.split()]
    
    if not prices:
        print("Profit: 0")
        return

    min_price = prices[0]
    max_profit = 0
    
    for price in prices:
        if price < min_price:
            min_price = price
        elif price - min_price > max_profit:
            max_profit = price - min_price
            
    print(f"Maximum Profit: {max_profit}")

stock_profit_efficient()

# Method - 2
def stock_profit_shortest():
    p = [float(x) for x in input("Enter daily stock prices (space separated):").split()]; m, r = float('inf'), 0
    for x in p: m = min(m, x); r = max(r, x - m)
    print(f"Maximum Profit: {r}")
stock_profit_shortest()

# Method - 3
def stock_profit_mathematical():
    raw = input("Enter prices: ").split()
    prices = []
    for item in raw:
        prices.append(float(item))
    
    if len(prices) < 2:
        print(0)
        return

    low_point = prices[0]
    best_gain = 0

    for i in range(1, len(prices)):
        current = prices[i]
        
        if current < low_point:
            low_point = current
        else:
            diff = current - low_point
            if diff > best_gain:
                best_gain = diff
                
    print(best_gain)

stock_profit_mathematical()