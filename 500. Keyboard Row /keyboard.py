from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        results = []

        for word in words:
            if all(ch.lower() in first_row for ch in word) or all(ch.lower() in second_row for ch in word) or all(ch.lower() in third_row for ch in word):
                results.append(word)
        return results


solution = Solution()
print(solution.findWords(["Hello", "Alaska", "Dad", "Peace"]))
