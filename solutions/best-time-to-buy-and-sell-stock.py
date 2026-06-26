from typing import List

# Examples:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1), sell on day 5 (price=6), profit = 5
#
# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: Prices only decrease, no profitable transaction possible

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        last_min_price = float('inf')
        sell = 0
        for price in prices:                
            if price < last_min_price:
                last_min_price = price
            elif sell < (price - last_min_price):
                sell = price - last_min_price
        return sell