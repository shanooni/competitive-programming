from typing import List


class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        n = len(nums)
        scores = []

        zeros = 0
        ones = 0

        for i in range(n + 1):
            nums_left = nums[:i]
            nums_right = nums[i:]

            if 0 in nums_left:
                zeros = nums_left.count(0)
            if 1 in nums_right:
                ones = nums_right.count(1)

                print(f"zero {zeros}")
                print(f"ones = {ones}")
                score = (zeros + ones)

            scores.append(score)
            print(f"score : {scores}")
        return [zeros, ones]


solution = Solution()

solution.maxScoreIndices([0, 0, 1, 0])
