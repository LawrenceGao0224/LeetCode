# 560. Subarray Sum Equals K
"""
Example 1:

Input: nums = [1,1,1], k = 2
Output: 2
Example 2:

Input: nums = [1,2,3], k = 3
Output: 2
"""

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        group = {0:1}
        res, sum0 = 0, 0
        for num in nums:
            sum0 += num
            res += group.get(sum0 - k, 0)
            group[sum0] = 1 + group.get(sum0, 0)
        return res

