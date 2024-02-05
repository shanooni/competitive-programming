from typing import List

"""
There is a programming language with only four operations and one variable X:

++X and X++ increments the value of the variable X by 1.
--X and X-- decrements the value of the variable X by 1.
Initially, the value of X is 0.

Given an array of strings operations containing a list of operations, return the final value of X after performing all the operations.
"""


def finalValueAfterOperations(operations: List[str]) -> int:
    results: int = 0
    for operation in operations:
        if operation == "++X" or operation == "X++":
            results += 1
        elif operation == "--X" or operation == "X--":
            results -= 1

    return results


print(finalValueAfterOperations(["--X", "X++", "X++"]))
print(finalValueAfterOperations(["++X", "++X", "X++"]))
print(finalValueAfterOperations(["X++", "++X", "--X", "X--"]))


"""
output:
1
3
0
"""