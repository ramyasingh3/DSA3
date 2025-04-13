"""
Problem: Coin Change Ways

Given a set of coin denominations and a target amount, find the number of different ways
to make change for the target amount using the given coins. You have an infinite supply
of each coin denomination.

Example:
coins = [1, 2, 5]
amount = 5
Output: 4
Explanation: The different ways are:
1. 1 + 1 + 1 + 1 + 1
2. 1 + 1 + 1 + 2
3. 1 + 2 + 2
4. 5
"""

from typing import List
from collections import defaultdict

def count_change_ways(coins: List[int], amount: int) -> int:
    """
    Count the number of different ways to make change for the target amount.
    Uses dynamic programming with space optimization.
    
    Time complexity: O(amount * len(coins))
    Space complexity: O(amount)
    """
    if not coins or amount < 0:
        return 0
    if amount == 0:
        return 1
    
    # dp[i] represents number of ways to make amount i
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: one way to make zero amount
    
    # For each coin, update the ways for all possible amounts
    for coin in coins:
        for current_amount in range(coin, amount + 1):
            dp[current_amount] += dp[current_amount - coin]
    
    return dp[amount]

def print_all_combinations(coins: List[int], amount: int) -> None:
    """
    Print all possible combinations to make the target amount.
    Uses backtracking to find all combinations.
    """
    def backtrack(remaining: int, current_combo: List[int], start_idx: int) -> None:
        if remaining == 0:
            print(" + ".join(map(str, current_combo)))
            return
        
        for i in range(start_idx, len(coins)):
            coin = coins[i]
            if remaining >= coin:
                current_combo.append(coin)
                backtrack(remaining - coin, current_combo, i)
                current_combo.pop()
    
    print(f"\nAll combinations for amount {amount}:")
    backtrack(amount, [], 0)

def test_coin_change():
    test_cases = [
        ([1, 2, 5], 5),
        ([2, 5, 10], 15),
        ([1, 2, 3], 4),
        ([2, 3, 5], 7),
        ([1], 5),
        ([5], 5),
        ([1, 2, 5], 0),
        ([2, 5], 3),  # Impossible case
        ([1, 2, 5], 10),
    ]
    
    for i, (coins, amount) in enumerate(test_cases, 1):
        print(f"\nTest {i}:")
        print(f"Coins: {coins}")
        print(f"Amount: {amount}")
        ways = count_change_ways(coins, amount)
        print(f"Number of ways: {ways}")
        
        # Only print combinations for smaller amounts to avoid too much output
        if amount <= 7:
            print_all_combinations(coins, amount)
        print("-" * 50)

if __name__ == "__main__":
    test_coin_change()
