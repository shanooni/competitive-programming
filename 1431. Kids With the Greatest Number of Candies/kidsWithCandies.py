from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxKidCandy = max(candies)
        results = []
        for candy in candies:
            if (candy + extraCandies) >= maxKidCandy:
                results.append(True)
            else:
                results.append(False)
        return results
