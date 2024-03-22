def minPairSum(nums: list[int]) -> int:
    n = len(nums)
    evenList = []
    oddList = []
    sumList = []
    for i in range(n):
        if i % 2 == 0:
            evenList.append(nums[i])
        else:
            oddList.append(nums[i])

    for i in range(n // 2):
        a = evenList[i]
        print(a)

        b = oddList[i]

        sum_ = a + b
        sumList.append(sum_)

    return max(sumList)


# print(minPairSum([3, 5, 2, 3]))


def minPairSumI(nums: list[int]) -> int:
    sortNums = sorted(nums)
    print(sortNums)
    half_len = len(nums) // 2
    sumList = []
    for i in range(half_len):
        a = sortNums[i]
        b = sortNums[-i - 1]
        sum_ = (a + b)

        print(sum_)
        sumList.append(sum_)
    return max(sumList)


minPairSumI([3, 5, 2, 3])
