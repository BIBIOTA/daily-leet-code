from typing import List

# Examples:
# Input: prices = [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy on day 2 (price=1), sell on day 5 (price=6), profit = 6-1 = 5
#
# Input: prices = [7, 6, 4, 3, 1]
# Output: 0
# Explanation: Prices only decrease, no profitable transaction possible

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        sell = 0
        for price in prices[1:]:
            if min_price > price:
                min_price = price
            if price - min_price > sell:
                sell = price - min_price
        return sell
            
