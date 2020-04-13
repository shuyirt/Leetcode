class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda item: item[0])
        i = 1
        while i < len(intervals):
            if intervals[i-1][1] >= intervals[i][0]:
                if intervals[i-1][1] < intervals[i][1]:
                    intervals[i-1][1] = intervals[i][1]
                del intervals[i]
            else:
                i += 1
        return intervals

# Runtime: 56 ms, faster than 62.72% of Python3 online submissions for Merge Intervals.
# Memory Usage: 14.2 MB, less than 93.54% of Python3 online submissions for Merge Intervals.
