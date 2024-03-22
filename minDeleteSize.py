from typing import List


class Solution:
    def minDeleteSize(self, strs: List[str]) -> int:
        x = 0
        for i in zip(*strs):
            if list(i) != sorted(i):
                x += 1
        return x


solution = Solution()

print(solution.minDeleteSize(["cba", "daf", "ghi"]))
