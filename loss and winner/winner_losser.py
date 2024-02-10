from typing import List


class Solution:
    def findWinner(self, matches: List[List[int]]) -> List[List[int]]:
        winners_dict = {}
        lossers_dict = {}
        lost_once = []

        for match in matches:
            winner = match[0]
            losser = match[1]
            winners_dict[winner] = winners_dict.get(winner, 0) + 1
            lossers_dict[losser] = lossers_dict.get(losser, 0) + 1

        winner = [win for win in winners_dict.keys() if win not in lossers_dict]

        for lossers, score in lossers_dict.items():
            if lossers not in winner and score <= 1:
                lost_once.append(lossers)
        return [sorted(winner), sorted(lost_once)]
