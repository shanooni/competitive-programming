"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
"""
from typing import List


def merge_string(word1: str, word2: str) -> str:
    index: int = 0
    result: List[str] = []
    while index < len(word1) or index < len(word2):
        if index < len(word1):
            result.append(word1[index])
        if index < len(word2):
            result.append(word2[index])
        index += 1
    return "".join(result)


print(merge_string("abc", "pqr"))
print(merge_string("ab", "pqrs"))
print(merge_string("abcd", "pq"))
