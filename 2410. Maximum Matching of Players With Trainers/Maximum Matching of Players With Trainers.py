class Solution:
    def matchPlayersAndTrainers(self, players: list[int], trainers: list[int]) -> int:

        trainers.sort()
        players.sort()
        i, j = 0, 0
        n, m = len(trainers), len(players)
        matchCount = 0
        while j < n and i < m:
            if players[i] <= trainers[j]:
                matchCount += 1
                i += 1
                j += 1
            else:
                j += 1
        print(f"max count is {matchCount}")
        return matchCount


solve = Solution()

solve.matchPlayersAndTrainers([4, 7, 9], [8, 2, 5, 8])
solve.matchPlayersAndTrainers([2], [1])
solve.matchPlayersAndTrainers([1, 1000000000], [1000000000, 1])  # 2
solve.matchPlayersAndTrainers([2, 1], [2, 1, 2, 2, 3, 3, 2, 4, 1, 1, 4, 1, 3, 3, 4, 1, 3, 2, 3, 2, 2, 3, 1, 2, 4])
solve.matchPlayersAndTrainers([2, 3, 1, 1, 3], [2, 4, 2]) # 3
