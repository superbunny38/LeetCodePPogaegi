class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        n_erase = 0
        prev_idx = 0
        for idx in range(1,len(intervals)):
            if intervals[prev_idx][1]>intervals[idx][0]:
                n_erase += 1
                
            else:
                prev_idx = idx
        return n_erase
