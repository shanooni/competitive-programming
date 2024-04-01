"""
Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

A subarray is a contiguous non-empty sequence of elements within an array.



Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        prefixSum: int = 0
        count: int = 0
        track = {0: 1}

        for num in nums:
            prefixSum += num

            if (prefixSum - k) in track:
                count += track[(prefixSum - k)]

            if prefixSum in track:
                track[prefixSum] += 1
            else:
                track[prefixSum] = 1
        return count


solution = Solution()
print(solution.subarraySum([1, 2, 3], 3))
