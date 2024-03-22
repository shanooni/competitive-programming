import math


class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        left: int = 0
        right: int = len(s) - 1
        res = []
        while left < right:
            print(f"l {left}")
            if s[left] != s[right]:
                right -= 1
            elif s[:right] not in s[right:]:
                right = len(s) - 1

            res.append(len(s[: right]))
        return res


solution = Solution()

print(solution.partitionLabels('ababcbacadefegdehijhklij'))
print(solution.partitionLabels('eccbbbbdec'))

