class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        people.sort()
        l, r = 0, len(people) - 1
        count = 0

        while l < r:
            if people[l] + people[r] <= limit:
                count += 1
                l += 1
                r -= 1
            else:
                r -= 1
        return len(people) - count


solve = Solution()

print(solve.numRescueBoats([3, 5, 3, 4], 5))
print(solve.numRescueBoats([3, 2, 2, 1], 3))
