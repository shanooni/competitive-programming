from typing import List


class Solution:
    def check(self, A: List[int], B: List[int], N: int) -> bool:
        if len(A) != N or len(B) != N:
            return int(False)

        sort_b = sorted(A)
        print(sort_b)
        sort_a = sorted(B)
        print(sort_a)
        return int(sort_a == sort_b)


solve = Solution()

print(solve.check([1, 2, 5], [2, 4, 15], 3))
print(solve.check([1, 2, 5, 4, 0], [2, 4, 5, 0, 1], 5))
