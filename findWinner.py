class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        players = [i for i in range(1, n+1)]
        while len(players) > 1:

            for _ in range(k - 1):
                print()
                players.append(players.pop(0))
            players.pop(0)
        return players[0]


solution = Solution()

solution.findTheWinner(5, 2)
