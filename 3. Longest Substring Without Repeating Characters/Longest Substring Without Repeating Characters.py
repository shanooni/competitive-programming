"""
Given a string s, find the length of the longest
substring
 without repeating characters.



Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

"""
using neetcode approach of sliding window and set
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lft = 0
        charSet = set()
        maxLen: int = 0
        for rgt in range(len(s)):
            while s[rgt] in charSet:
                charSet.remove(s[lft])
                lft += 1
            charSet.add(s[rgt])
            maxLen = max(maxLen, rgt - lft + 1)

        return maxLen

solution = Solution()

print(solution.lengthOfLongestSubstring("abcabcbb"))
print(solution.lengthOfLongestSubstring("bbbbb"))
