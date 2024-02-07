from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word2) == "".join(word1)


print(Solution().arrayStringsAreEqual(["jbboxe", "yshcrtanrtlzyyp", "vudsssnzuef", "lde"],
                                      ["jbboxeyshcrtanrt", "lzyypvudsssnzueflde"]))  # True
print(Solution().arrayStringsAreEqual(["a", "cb"], ["ab", "c"]))  # False
