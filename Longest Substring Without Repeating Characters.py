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

#############################################################################################

# 424. Longest Repeating Character Replacement

# Input:  s = "ABAB", k = 2

    def characterReplacement(self, s: str, k: int) -> int:
        Windowstart 0
        char_freq = {}
        longest = 0
        maxrepeatchar = 0
        for Windowend in range(len(s)):
            if s[Windowend] not in char_freq:
                char_freq[s[Windowend]] = 0

            char_freq[s[Windowend]] += 1
            maxrepeatchar = max(maxrepeatchar, char_freq[s[Windowend]])

            if ( Windowend - Windowstart + 1) - maxrepeatchar > k : # 目前長度 - 最大重複 > 可變更數  Ex: ABBB 最大重複為 B:3 ， 4-3 > 1:（False) 則可接受 
                char_freq[s[Windowstart]] -= 1
                Windowstart += 1

            longest = max(longest, ( Windowend - Windowstart + 1))  
        return longest

#########################################################################################
# 76. Minimum Window Substring

#Input: s = "ADOBECODEBANC", t = "ABC"
#Output: "BANC"
    def minWindow(self, s: str, t: str) -> str:
        if not t : return ""
        window, count_t = {}, {}
        for c in t:
            count_t[c] = 1 + count.get(c,0)
        l = 0
        res, reslen = [-1,-1], len(s) + 1
        have, need = 0, len(count_t)
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c,0)

            if c in count_t and count_t[c] == window[c]:
                have += 1
            
            while have == need :
                if (r - l + 1) < reslen:
                    reslen = r - l + 1
                    res = [l, r]
                window[s[l]] -= 1
                if s[l] in count_t and count_t[s[l]] > window[s[l]] :
                    have -= 1 
                l += 1
        l, r = res
        return s[l:r+1] if reslen != len(s) + 1 else ""

             