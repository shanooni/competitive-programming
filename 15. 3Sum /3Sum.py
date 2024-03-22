class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        res = set()

        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if nums[i] + nums[j] + nums[k] == 0:
                        r = tuple((sorted([nums[i], nums[j], nums[k]])))
                        res.add(r)
        return [list(r) for r in res]


solve = Solution()

print(solve.threeSum([-1, 0, 1, 2, -1, -4]))
