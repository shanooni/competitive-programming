from typing import List


class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        operation_dict = {num: ind for ind, num in enumerate(nums)}

        for op1, op2 in operations:
            nums[operation_dict[op1]] = op2
            operation_dict[op2] = operation_dict[op1]

        return nums
