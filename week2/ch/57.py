class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        ret = []
        new_start,new_end = newInterval[0],newInterval[1]
        if intervals == []:
            return [newInterval]
        def merge(interval1,interval2):
            return min(interval1[0],interval2[0]),max(interval1[1],interval2[1])
        is_new_handled = False
        for idx,interval in enumerate(intervals):
            # print(f"idx:{idx} || {interval}")
            # print(f"newinterval:{new_start},{new_end}")
            if is_new_handled == False:
                if interval[1]<new_start:
                    # print("1")
                    ret.append(interval)
                    continue
                elif new_start<=interval[0] and interval[1]<=new_end:
                    # print("2")
                    continue
                elif (interval[0]<=new_start<=interval[1] or interval[0]<=new_end<=interval[1]):
                    # print("3")
                    new_start, new_end = merge(interval,[new_start,new_end])
                    continue
                else:
                    ret.append([new_start,new_end])
                    ret.append(interval)
                    is_new_handled = True
                    new_start,new_end = None,None
            else:
                ret.append(interval)
                    

        if is_new_handled == False:
            ret.append([new_start,new_end])

        
        return ret

