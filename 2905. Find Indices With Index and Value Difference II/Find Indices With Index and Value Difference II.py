class Solution:
    def findIndices(self, nums: list[int], indexDifference: int, valueDifference: int) -> list[int]:
        i, j = 0, len(nums) - 1
        ans = []

        while i <= j:
            if abs(i - j) >= indexDifference and abs(nums[i] - nums[j]) >= valueDifference:
                ans.append(i)
                ans.append(j)
                i += 1
            j -= 1
        return ans


solution = Solution()
solution.findIndices([5, 1, 4, 1], 2, 4)
solution.findIndices([2, 1], 0, 0)
solution.findIndices([1, 2, 3], 2, 4)
