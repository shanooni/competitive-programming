from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        sortedList = sorted(strs)
        first_string = sortedList[0]
        last_string = sortedList[-1]

        for i in range(min(len(first_string), len(last_string))):
            if first_string[i] != last_string[i]:
                return prefix
            prefix += first_string[i]
        return prefix


solve = Solution()
print(solve.longestCommonPrefix(["flower", "flow", "flight"]))
print(solve.longestCommonPrefix(["dog", "racecar", "car"]))
print(solve.longestCommonPrefix(["cir", "car"]))
