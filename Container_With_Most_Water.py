# 11. Container With Most Water

'''

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
In this case, the max area of water (blue section) the container can contain is 49.

'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        water = 0
        left = 0
        right = len(height) - 1
        while left < right:
            width = right - left
            if height[left] > height[right]:
                res =  width * height[right]
                right -= 1
            else:
                res = width * height[left]
                left += 1
            if res > water:
                water = res
        return water
            