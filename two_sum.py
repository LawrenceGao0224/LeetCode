from typing import List

class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        sort_nums = sorted(nums)
        l = 0
        r = len(sort_nums)-1
        while r > l:
            summ = sort_nums[l] + sort_nums[r]
            if summ > target:
                r -= 1
            elif summ < target:
                l += 1
            else:
                break
        # sort_nums[l],sort_nums[r]
        res = []
        for i in range(len(nums)):
            if nums[i] == sort_nums[l] or nums[i] == sort_nums[r]:
                res.append(i)
            if len(res) == 2:
                break
            else:
                continue
        return(res)
        
number = [2,7,11,5]
target = 9
a = Solution()
print(a.twoSum(number,target))

