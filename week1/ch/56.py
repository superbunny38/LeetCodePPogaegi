class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals)
        ret = [intervals.pop(0)]

        for interval in intervals:
            last = ret[-1]
            if interval[0] <= last[-1]:
                ret[-1][1] = max(interval[1],last[-1])
            else:
                ret.append(interval)
        return ret
