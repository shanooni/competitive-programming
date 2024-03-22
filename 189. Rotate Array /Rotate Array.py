class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # i = 0
        # n = len(nums)
        # while k +1 < n:
        #     print(f"i is {i}")
        #     print(f"k : {k}")
        #     nums[i], nums[k+1] = nums[k+1], nums[i]
        #
        #     i += 1
        #     k += 1
        # print(nums)
        if k % 2 == 1:
            c = nums[:k + 1]
            d = nums[k + 1:]
            print(d + c)
        else:
            c = nums[:k]
            d = nums[k:]
            print(d + c)


solve = Solution()

solve.rotate([1, 2, 3, 4, 5, 6, 7], 3)
solve.rotate([-1, -100, 3, 99], 2)

# [5,6,7,1,2,3,4]    #correct
# [4,5,6,7,2,3,1] #my results
