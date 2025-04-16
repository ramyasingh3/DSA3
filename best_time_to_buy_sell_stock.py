from typing import List

def max_profit(prices: List[int]) -> int:
    """
    Calculate the maximum profit from buying and selling stock.
    
    Args:
        prices: List of stock prices for each day
        
    Returns:
        Maximum profit achievable
    """
    if not prices:
        return 0
        
    min_price = float('inf')
    max_profit = 0
    
    for price in prices:
        # Update minimum price if current price is lower
        min_price = min(min_price, price)
        # Calculate potential profit and update max profit
        max_profit = max(max_profit, price - min_price)
    
    return max_profit

def test_max_profit():
    """Test cases for the max profit solution."""
    
    test_cases = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
        ([1], 0),
        ([2, 4, 1], 2),
        ([3, 2, 6, 5, 0, 3], 4),
        ([2, 1, 2, 1, 0, 1, 2], 2)
    ]
    
    print("Testing Best Time to Buy and Sell Stock Solution...")
    for prices, expected in test_cases:
        result = max_profit(prices)
        print(f"\nInput: prices = {prices}")
        print(f"Expected: {expected}")
        print(f"Got: {result}")
        print(f"Test {'passed' if result == expected else 'failed'}")
        print("-" * 50)

if __name__ == "__main__":
    test_max_profit() 