class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        starts = sorted([interval[0] for interval in intervals])
        ends = sorted([interval[1] for interval in intervals])
        start_ptr, end_ptr = 0, 0
        rooms, max_rooms = 0, 0
        while start_ptr < len(intervals) and end_ptr < len(intervals):
            if starts[start_ptr] < ends[end_ptr]:
                rooms += 1
                max_rooms = max(max_rooms, rooms)
                start_ptr += 1
            elif starts[start_ptr] > ends[end_ptr]:
                rooms -= 1
                end_ptr += 1
            else:
                start_ptr += 1
                end_ptr += 1
        return max_rooms
            
