# 347. Top K Frequent Elements

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        group = {}
        
        for c in nums:
            if c in group:
                group[c] += 1
            else:
                group[c] = 1
                
        res = sorted(group, key=lambda x: -group[x])
        
        
        return res[:k]
    