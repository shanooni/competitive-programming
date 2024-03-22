from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        results = []
        for i, ball in enumerate(boxes):
            if ball == '1':
                answer.append(i)

        for j in range(len(boxes)):
            moves = 0
            for i in answer:
                moves += abs(j - i)
            results.append(moves)

        print(results)


solution = Solution()
solution.minOperations("110")
