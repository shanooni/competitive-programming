from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        half_len = len(nums) // 2
        postives = []
        negatives = []
        results = []
        for i in range(len(nums)):
            if "-" in str(nums[i]):
                negatives.append(nums[i])
            else:
                postives.append(nums[i])
        print(postives)
        print(negatives)
        for i in range(half_len):
            results.append(postives[i])
            results.append(negatives[i])
        return results


print(Solution().rearrangeArray([3, 1, -2, -5, 2, -4]))
