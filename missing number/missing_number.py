from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hashmap = {}

        for num in range(len(nums) + 1):
            if num in nums:
                hashmap[num] = 1
            else:
                hashmap[num] = 0
        for key, value in hashmap.items():
            if value == 0:
                return key
