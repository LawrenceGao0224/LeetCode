"""
The idea is to use the original array to keep track of the numbers visited. Since all the numbers are positive intergers, for every number visited we mark the presence of that number by negating the number at the index equal to the current number. Since Python follows 0-indexing, the index we mark is actually number - 1. If the number at that index is already negated we do nothing. In the end, we just return the indices (index + 1 for the number) where there are still postive numbers.

Still confused?? I hope the following example will make it clearer:
Let nums = [4, 3, 2, 7, 8, 2, 3, 1]. Now let's iterate through the array nums.

At iter = 0,
current number: |4| (|.| here refers to taking the absolute value)
number at index = 3 (current number - 1): 7
After negation: nums = [4, 3, 2, -7, 8, 2, 3, 1]

At iter = 1
current number: |3|
number at index = 2: 2
After negation: nums = [4, 3, -2, -7, 8, 2, 3, 1]

At iter = 2
current number: |-2|
number at index = 1: 3
After negation: nums = [4, -3, -2, -7, 8, 2, 3, 1]

At iter = 3
current number: |-7|
number at index = 6: 3
After negation: nums = [4, -3, -2, -7, 8, 2, -3, 1]

At iter = 4
current number: |8|
number at index = 7: 1
After negation: nums = [4, -3, -2, -7, 8, 2, -3, -1]

At iter = 5
current number: |2|
number at index = 1: -3
Array stays unchanged: nums = [4, -3, -2, -7, 8, 2, -3, -1]

At iter = 6
current number: |-3|
number at index = 2: -2
Array stays unchanged: nums = [4, -3, -2, -7, 8, 2, -3, -1]

At iter = 7
current number: |-1|
number at index = 0: 4
After negation: nums = [-4, -3, -2, -7, 8, 2, -3, -1]
"""
"""
Example:

Input:
[4,3,2,7,8,2,3,1]

Output:
[5,6]
"""


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        
        for i in range(len(nums)):
            temp = abs(nums[i]) - 1
            if nums[temp] > 0:
                nums[temp] *= -1
            
        res = []
        for i in range(len(nums)):
            if nums[i] > 0:
                res.append(i+1)
        return res
