from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        best = left = 0
        right = len(height) - 1
        while right > left:
            min_point = min(height[left], height[right])
            distance = right - left
            area = min_point * distance
            best = max(best, area)
            if min_point == height[left]:
                left += 1
            else:
                right -= 1
        return best


# Examples:
# height = [1, 8, 6, 2, 5, 4, 8, 3, 7] -> 49
# height = [1, 1] -> 1
