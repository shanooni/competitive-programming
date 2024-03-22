from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        sort_nums = []
        for num in arr2:
            while num in arr1:
                sort_nums.append(num)
                arr1.remove(num)
        return sort_nums + sorted(arr1)
