from typing import List


class Solution:
    def findWinner(self, matches: List[List[int]]) -> List[List[int]]:
        lossers = {}
        winners = set()
        lost_once = []

        for winner, losser in matches:
            winners.add(winner)
            lossers[losser] = lossers.get(losser, 0) + 1
        print(winners)
        print(lossers)
        for losser, score in lossers.items():
            if score <= 1:
                lost_once.append(losser)
            if losser in winners:
                winners.remove(losser)
        return [sorted(winners), sorted(lost_once)]


solution = Solution()
print(solution.findWinner([[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [4, 9], [10, 4], [10, 9]]))
