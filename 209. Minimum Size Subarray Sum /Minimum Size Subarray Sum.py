class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:

        minSum = 0
        count = 0
        n = len(nums)
        lft = 0
        if sum(nums) < target:
            return 0
        for rgt in range(n):
            minSum += nums[rgt]
            while minSum >= target:
                minSum -= nums[lft]
                lft += 1
            count += rgt - lft + 1
        return count


solve = Solution()

print(solve.minSubArrayLen(11, [1, 2, 3, 4, 5]))
print(solve.minSubArrayLen(4, [1, 4, 4]))
print(solve.minSubArrayLen(11, [1, 1, 1, 1, 1, 1, 1, 1]))
print(solve.minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
