class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        intervals.sort(key = lambda x:x[1])
        schedule = []
        for interval in intervals:
            if len(schedule) == 0:
                schedule.append(interval)
            else:
                last_finished = schedule[-1][1]
                if last_finished>interval[0]:
                    return False
                else:
                    schedule.append(interval)
        return True
