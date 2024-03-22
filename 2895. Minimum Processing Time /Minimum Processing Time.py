def minProcessingTime(processorTime: list[int], tasks: list[int]) -> int:
    half_len = len(tasks) // 2
    sortTasks = sorted(tasks)
    largestTask = []
    lowestTask = []
    min_processor = min(processorTime)
    max_processor = max(processorTime)
    for i in range(half_len):
        largestTask.append(sortTasks[-i - 1] + min_processor)
        lowestTask.append(sortTasks[i] + max_processor)
    return max(max(lowestTask), max(largestTask))


print(minProcessingTime([8, 10], [2, 2, 3, 1, 8, 7, 4, 5]))
