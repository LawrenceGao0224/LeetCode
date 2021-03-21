# 849. Maximize Distance to Closest Person
'''
Input: seats = [1,0,0,0,1,0,1]
Output: 2

We iterate i over range(len(seats)), 
and initialize prev = None, 
which records the index of the previous 1,
and the solution of the problem res = -float('inf'). 
If seats[i] == 1, and prev == None, 
it means that we encounter the first seated person (e.g., we meet the 1 in such configuration [0,0,1,....]), 
then the current largest distance is i, which can be achieved by sitting at the leftmost seat, 
and we update res = i, prev = i. If seats[i] == 1, 
and prev != None, it means that we encounter at least two persons already (e.g., we meet the second 1 in such configuration [...,1,0,0,0,1,...]), 
the by sitting in the middle of the i and prev, we maximize the minimum distance between the nearest person, which is (i-prev) // 2, we update res = max(res, (i-prev) // 2), a
nd prev = i. Finally, after iterating i over range(len(seats)), we also need to consider the possibility of sitting at the rightmost seat (e.g., in such configuration [...,1,0,0,0]), and we need to make a final update of res by res = max(res, len(seats)-1-prev). Then we return res.
'''

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        
        prev = None
        res = 1
        for i in range(len(seats)):
            if seats[i] == 1:
                if prev == None:
                    res = i
                    prev = i
                else:
                    res = max( res, (i-prev)//2 )
            prev = i
        res = max(res, len(seats) - prev - 1)
        return res