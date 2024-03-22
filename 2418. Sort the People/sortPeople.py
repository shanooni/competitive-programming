from typing import List


class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        height_names_dict = zip(heights, names)
        sort_dict = sorted(height_names_dict, reverse=True)
        return [name for height, name in sort_dict]
