class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        s_set = set()
        l = 0
        res = 0
        for i in range(len(s)):
            while s[i] in s_set:
                s_set.remove(s[l])
                l += 1
            s_set.add(s[i])
            res = max(res, i-l+1)
        return res
s = "abcabcbb"
a = Solution()
print(a.lengthOfLongestSubstring(s))