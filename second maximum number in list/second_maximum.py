from typing import List


def second_max(nums: List[int]):
    # check to remove duplicates from list and sort in reverse
    reverseSortList = sorted(set(nums), reverse=True)
    if len(reverseSortList) > 1:
        runner_up = reverseSortList[1]
    return runner_up


if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    lst = list(arr)
    print(second_max(lst))

