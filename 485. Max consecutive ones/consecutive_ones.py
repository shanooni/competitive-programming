from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        results = []

        for i in range(len(nums) - 1):
            if nums[i + 1] == nums[i]:
                results.append(nums[i])
            else:
                results.clear()
        print(results)
        return len(results)


print(Solution().findMaxConsecutiveOnes([1, 1, 0, 1, 1, 1]))
print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1]))
