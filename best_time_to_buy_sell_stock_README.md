# Best Time to Buy and Sell Stock

## Problem Description
Given an array `prices` where `prices[i]` is the price of a given stock on the ith day, find the maximum profit you can achieve by buying on one day and selling on a later day. If you cannot achieve any profit, return 0.

### Examples
```
Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
```

## Approach
1. Keep track of the minimum price seen so far
2. For each price:
   - Calculate potential profit (current price - minimum price)
   - Update maximum profit if current profit is higher
   - Update minimum price if current price is lower

### Key Points
- One-pass solution
- O(1) space complexity
- Handles edge cases (decreasing prices, single day)
- No need to store all prices

## Time Complexity
- O(n) where n is the length of the prices array
  - We traverse the array exactly once

## Space Complexity
- O(1) constant space
  - We only store min_price and max_profit 