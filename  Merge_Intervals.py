# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        temp = []
        merge = []
        intervals.sort()
        merge = intervals[0]
        for i in range(1, len(intervals)):
            # [0,4], [2,3]
            if merge[0] <= intervals[i][0] and merge[1] >= intervals[i][1]:
                continue
            # [1,3], [2,4]
            elif merge[1] >= intervals[i][0]:
                merge = [merge[0], intervals[i][1]]
            else:
                temp.append(merge)
                merge = intervals[i]
        temp.append(merge)
        return temp