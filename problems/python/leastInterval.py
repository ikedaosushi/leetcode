from typing import List
from collections import Counter


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        tasks_counts = list(Counter(tasks).values())
        max_ = max(tasks_counts)
        max_count = tasks_counts.count(max_)
        return max(len(tasks), (max_ - 1) * (n + 1) + max_count)


if __name__ == "__main__":
    Solution().leastInterval(["A", "A", "A", "B", "B", "B"], 2)
