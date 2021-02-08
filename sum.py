# Two Sum

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


#===========================================================================================================

# 15. 3Sum

    def threeSum(self, nums):
        nums.sort()
        ans = []

        if len(nums) < 3:
            return ans

        for i in range(len(nums)):
            if i >= 1 and nums[i-1] == nums[i]:
                continue

            left = i + 1
            right = len(nums) -1

            while left < right:
                sum3 = nums[i] + nums[left] + nums[right]
                if sum3 < 0:
                    left += 1
                    
                elif sum3 > 0:
                    right -= 1

                else:
                    ans.append([nums[i], nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
        return ans 

# 18. 4Sum

