class Solution:
    def freq_Alphabets(self, s: str) -> str:
        for i in range(26, 0, -1):
            s = s.replace(str(i) + '#' * (i > 9), chr(96 + i))
        return s
