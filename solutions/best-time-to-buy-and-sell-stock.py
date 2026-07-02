from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Examples:
        # Input: prices = [7, 1, 5, 3, 6, 4]  → Output: 5
        # Input: prices = [7, 6, 4, 3, 1]      → Output: 0
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit
