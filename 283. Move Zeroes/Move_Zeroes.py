class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        s = 0
        ph = 0

        if len(nums) == 1:
            return nums

        while s < len(nums):
            if nums[s] == 0:
                nums[ph], nums[s] = nums[s+1], nums[ph]
                ph += 1
            s += 1
            print(nums)
        return nums


solve = Solution()

# solve.moveZeroes([0, 1, 0, 3, 12])
solve.moveZeroes([ 1, 0, 1])
