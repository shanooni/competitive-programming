"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.
"""


def palindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


print(palindrome(121))
