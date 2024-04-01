"""
find the sub array where the subarray is minimal
sum = 15
num = {5, 1, 3, 5, 10, 7, 4,9, 2, 8}
"""
import math


def dynamicSliding(sums: int, nums: list[int]) -> list[int]:
    lft = 0
    sum_ = 0
    res = math.inf
    for rgt in range(len(nums)):
        sum_ += nums[rgt]
        print(f" sum : {sum_}")
        while sum_ >= sums:
            res = min(res, rgt - lft + 1)
            lft += 1
            sum_ -= nums[lft]
    return res


print(dynamicSliding(15, [5, 1, 3, 5, 10, 7, 4, 9, 2, 8]))
