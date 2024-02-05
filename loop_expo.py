"""
Task
The provided code stub reads and integer, , from STDIN. For all non-negative integers , print .

Example
n = 3
The list of non-negative integers that are less than 3 is [0,1,2].
Print the square of each number on a separate line.
0
1
4
"""


def loop_exponent(num: int) -> list[int]:
    answer: list[int] = []
    if num < 0:
        return
    else:
        for index in range(num):
            answer.append(index ** 2)
    return answer


if __name__ == '__main__':
    n = int(input())
    print(loop_exponent(n))

