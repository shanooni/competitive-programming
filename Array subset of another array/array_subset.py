from typing import List


def isSubset(a1: List[int], a2: List[int], n: int, m: int) -> str:
    set_a1 = set(a1)
    set_a2 = set(a2)

    if len(set_a1) != n or len(set_a2) != m:
        return "No"
    if set_a2.issubset(set_a1):
        return "Yes"
    return "No"


print(isSubset([1, 2, 3, 4, 5, 6, 7, 8], [1, 2, 3, 1], 8, 4))  # No
print(isSubset([11, 1, 13, 21, 3, 7], [11, 3, 7, 1], 6, 4))  # Yes
