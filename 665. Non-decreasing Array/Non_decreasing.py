from typing import List


class Solution:
    def non_decreasing(self, nums: List[int]) -> bool:
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                return True
        return False


solution = Solution()
print(solution.non_decreasing([4, 2, 3]))
print(solution.non_decreasing([4, 2, 1]))
print(solution.non_decreasing([3, 4, 2, 3]))  # false
