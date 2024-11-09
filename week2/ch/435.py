class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[1])
        print("intervals:",intervals)
        def merge(interval1,interval2):
            return min(interval1[0],interval2[0]),max(interval1[1],interval2[1])

        ret = []
        change_count = 0
        for interval in intervals:
            if len(ret) == 0:
                ret.append(interval)
            else:
                last_elem = ret[-1][1]
                if interval[0]<last_elem:
                    print("remove:",interval)
                    change_count+=1
                    continue
                else:
                    ret.append(interval)
                
        return change_count
