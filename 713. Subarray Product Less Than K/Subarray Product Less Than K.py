""""
Given an array of integers nums and an integer k, return the number of contiguous
subarrays where the product of all the elements in the subarray is strictly less than k.


Example 1:

Input: nums = [10,5,2,6], k = 100
Output: 8
Explanation: The 8 subarrays that have product less than 100 are:
[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
Example 2:

Input: nums = [1,2,3], k = 0
Output: 0
"""


# approach:
# given [10,5,2,6], k = 100
# thinking of sorting in ascending order
# first check if the ith elements are strictly less than k increase count by
# second check if pairs products of ith and i+1th are less than k increase count
# continue until the entire arr is checked

class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        prod: int = 1
        n: int = len(nums)
        count: int = 0
        lft: int = 0

        if k <= 1:
            return 0

        for rgt in range(n):
            prod *= nums[rgt]
            while prod >= k:
                prod /= nums[lft]
                lft += 1
            count += rgt - lft + 1
        return count


solution = Solution()
print(solution.numSubarrayProductLessThanK([10, 5, 2, 6], 100))
