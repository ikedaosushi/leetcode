class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 0:
            return intervals

        intervals = sorted(intervals, key=lambda i: i[0])
        merged = [intervals[0]]

        for interval in intervals[1:]:
            if merged[-1][1] >= interval[0]:
                merged[-1] = [merged[-1][0], max(merged[-1][1], interval[1])]
            else:
                merged.append(interval)

        return merged
