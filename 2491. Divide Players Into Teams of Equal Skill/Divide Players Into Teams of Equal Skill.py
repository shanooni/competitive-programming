class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        skill.sort()
        l = 0
        r = len(skill) - 1
        sum_list = []
        prod_list = []
        while l <= r:
            sum_ = skill[l] + skill[r]
            print(f"sum_ : {sum_}")
            l += 1
            r -= 1
        sum_list.append(sum_)

        if len(set(sum_list)) == 1:
            prod = skill[l] * skill[r]
            print(f"prod: {prod}")
        prod_list.append(prod)

        return max(prod_list)


solve = Solution()
print(solve.dividePlayers([3, 2, 5, 1, 3, 4]))
# skill = [3, 2, 5, 1, 3, 4]
# sort = [1,2,3,3,4,5]

#
# Explanation:
# Divide the players into the following teams: (1, 5), (2, 4), (3, 3), where each team has a total skill of 6.
# The sum of the chemistry of all the teams is: 1 * 5 + 2 * 4 + 3 * 3 = 5 + 8 + 9 = 22.
# l = 0
# r = len(skill) - 1
# skill.sort()
# results = []
# while l < r:
#     mult = skill[l] * skill[r]
#     results.append(mult)
#
#     l += 1
#     r -= 1
# return sum(results)
