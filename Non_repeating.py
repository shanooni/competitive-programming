from collections import Counter


class Solution:
    def firstUniqueString(self, s: str) -> int:
        count_s = Counter(s)

        for i in range(len(s)):
            current_element = s[i]
            if count_s[current_element] == 1:
                return i
        return -1


solution = Solution()
print(solution.firstUniqueString("leetcode"))
print(solution.firstUniqueString("loveleetcode"))
print(solution.firstUniqueString("aabb"))
