# MEETING ROOMS
# [(0,30), (5,10), (15,30) Can one person join all meeting
class Solution:
    def CanAttendingmeeting(self, intervals: List[List[int]]) -> bool
        start = []
        end = []
        for i in range(len(intervals)):
            start.append(intervals[i][0])
            end.append(intervals[i][1])
        start.sort()
        end.sort()
        for i in range(len(intervals)-1):
            if end[i] < start[i+1]:
                continue
            else:
                return False
        return True

        #==============  改良 =====================

        intervals.sort()
        last_end = -1
        for start, end in intervals:
            if start >= last_end:
                last_end = end
            else:
                return False
        return True

# MEETING ROOMS II
# [(0,30), (5,10), (15,30) --> Total meeting rooms = 2

import heapq
    def meetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        heap = [] # Store end time, pop the earliest , heap 存放每個 meeting room 的 end time
        rooms = 1
        heapq.heappush(heap, intervals[0][1])
        for start, end in intervals[1:]:
            if heap[0] <= start:
                heapq.heappop(heap)
            headq.headpush(heap, end)
            rooms = max(rooms, len(heap))
        return rooms
