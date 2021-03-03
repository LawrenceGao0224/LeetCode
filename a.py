# [(0,30), (5,10), (15,30) --> Total meeting rooms = 2

import heapq
from typing import List

class Solution:
    def meetingRooms(self, intervals: List[List[int]]) -> int:
        
        intervals.sort()
        heap = []
        rooms = 1
        heapq.heappush(heap, intervals[0][1])
        for start, end in intervals[1:]:
            if start >= heap[0]:
                heapq.heappushpop(heap, end)
            else:
                heapq.heappush(heap, end)
            rooms = max(rooms, len(heap))
        return rooms
intervals = [(0,30), (5,10), (15,30)]
a = Solution()
print(a.meetingRooms(intervals))