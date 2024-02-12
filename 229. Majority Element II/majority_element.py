from collections import Counter
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        results = []
        map_counter = Counter(nums)

        threshold = len(nums) // 3

        for key, count in map_counter.items():
            if count > threshold:
                results.append(key)
        return results

