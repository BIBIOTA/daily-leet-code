from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_price = float('inf')
        for price in prices:
            min_price = min(price, min_price)
            max_profit = max(max_profit, price - min_price)
        return max_profit


# Examples:
# Input: prices = [7, 1, 5, 3, 6, 4]  -> Output: 5
#   (買在第2天價格1，賣在第5天價格6，利潤 = 6 - 1 = 5)
#
# Input: prices = [7, 6, 4, 3, 1]     -> Output: 0
#   (價格持續下跌，無法獲利，回傳 0)
