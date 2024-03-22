from math import sqrt


class Solution:
    def judgeSquareSum(self, c: int) -> bool:

        i = 0
        j = int(sqrt(c))
        while i <= j:
            sum_sqr = (i ** 2) + (j ** 2)
            if sum_sqr == c:
                return True
            if sum_sqr > c:
                j -= 1
            else:
                i += 1
        return False


solve = Solution()
# solve.judgeSquareSum(5)
# solve.judgeSquareSum(4)
print(solve.judgeSquareSum(10000))
print(solve.judgeSquareSum(1))

