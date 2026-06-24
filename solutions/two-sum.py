from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result_dict = {}
        for index,num in enumerate(nums):
            diff = target - num
            if diff in result_dict:
                return [result_dict[diff], index]
            result_dict[num] = index


# Examples:
# Input: nums = [2, 7, 11, 15], target = 9  -> Output: [0, 1]  (因為 nums[0] + nums[1] = 9)
# Input: nums = [3, 2, 4],      target = 6  -> Output: [1, 2]
# Input: nums = [3, 3],         target = 6  -> Output: [0, 1]
