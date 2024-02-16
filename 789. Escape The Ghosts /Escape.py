from typing import List


class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        target_row = target[0]
        target_col = target[-1]

        player_target_distance = abs(target_row) + abs(target_col)

        for ghost in ghosts:
            ghost_target_distance = abs(target_row - ghost[0]) + abs(target_col - ghost[-1])

            if ghost_target_distance <= player_target_distance:
                return False
        return True

