from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNum = list(set(nums))
        return sorted(setNum) != sorted(nums)


solve = Solution()
print(solve.containsDuplicate([1, 2, 3, 4]))
print(solve.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))
print(solve.containsDuplicate([3, 1]))
