# 300. Longest Increasing Subsequence
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def Binarysearch(res, num):
            left = 0
            right = len(res) - 1 
            while left <= right:
                mid = left + (right - left) // 2
                if res[mid] > num:
                    right = mid - 1
                elif res[mid] < num:
                    left = mid + 1
                else:
                    return mid
            return left
        res = []
        for num in nums:
            pos = Binarysearch(res, num)
            if pos == len(res):
                res.append(num)
            else:
                res[pos] = num
        return len(res)
