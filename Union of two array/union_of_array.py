from typing import List


class Solution:
    def doUnion(self, a, n, b, m):
        union_set = set()
        set_a = set(a)
        set_b = set(b)

        if len(a) == n and len(b) == m:
            union_set = set_a | set_b

        return len(union_set)


solve = Solution()
print(solve.doUnion([1, 2, 3, 4, 5], 5, [1, 2, 3], 3)) #5
print(solve.doUnion([85, 25, 1, 32, 54, 6], 6, [85, 2], 2)) #7
