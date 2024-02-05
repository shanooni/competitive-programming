from typing import List


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        count: int = 0
        for i in range(0, len(nums)):
            for j in range((i + 1), len(nums)):
                if nums[i] == nums[j] and i < j:
                    count += 1
        return count


print(Solution().numIdenticalPairs([1, 2, 3, 1, 1, 3]))
