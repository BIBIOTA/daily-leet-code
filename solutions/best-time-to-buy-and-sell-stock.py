from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Examples:
        # Input: prices = [7, 1, 5, 3, 6, 4]
        # Output: 5  (第2天買入價格1，第5天賣出價格6，利潤 = 6-1 = 5)
        #
        # Input: prices = [7, 6, 4, 3, 1]
        # Output: 0  (價格持續下跌，無法獲利)
        buy = float('inf')
        max_profit = 0
        for price in prices:
            buy = min(price, buy)
            max_profit = max(max_profit, price - buy)
        return max_profit
