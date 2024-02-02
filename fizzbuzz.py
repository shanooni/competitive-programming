"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    answer: List[str] = []
    for i in range(n+1):
        if i % 3 == 0 and i % 5:
            answer.append("fizzbuzz")
        elif i % 3 == 0:
            answer.append("Fizz")
        elif i % 5 == 0:
            answer.append("Buzz")
        else:
            answer.append(str(i))

    return answer


print(fizzbuzz(5))

"""
output:
['Fizz', '1', '2', 'fizzbuzz', '4', 'Buzz']
"""