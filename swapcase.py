"""
You are given a string and your task is to swap cases.
In other words, convert all lowercase letters to uppercase letters and vice versa.
"""


def swap_case(s: str) -> str:
    return s.swapcase()


if __name__ == '__main__':
    print(swap_case("Www.HackerRank.com"))
