# 121. Best Time to Buy and Sell Stock — Easy
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
#
# Find the max profit from one buy/sell. Must buy before selling.
#
# Approach: single pass — track min price seen so far, compute profit at each step.
# Time: O(n)  Space: O(1)

from typing import List


def max_profit(prices: List[int]) -> int:
    min_price  = float('inf')
    max_profit = 0
    for price in prices:
        min_price  = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit


if __name__ == "__main__":
    assert max_profit([7,1,5,3,6,4]) == 5
    assert max_profit([7,6,4,3,1])   == 0
    assert max_profit([1,2])         == 1
    print("All tests passed.")
