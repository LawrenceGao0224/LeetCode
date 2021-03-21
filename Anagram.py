# 242. Valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = "".join(sorted(s))
        sort_t = "".join(sorted(t))
        
        return (sort_s == sort_t)

#==========================================================================================

# 49. Group Anagrams

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        if not strs:
            return strs

        for s in strs:
            sort_s = "".join(sorted(s))
            if sort_s in group:
                group[sort_s].append(s)
            else:
                group[sort_s] = [s]
        return group.values()

#==========================================================================================
# 1160. Find Words That Can Be Formed by Characters

'''
Example 1:

Input: words = ["cat","bt","hat","tree"], chars = "atach"
Output: 6
Explanation: 
The strings that can be formed are "cat" and "hat" so the answer is 3 + 3 = 6.
Example 2:

Input: words = ["hello","world","leetcode"], chars = "welldonehoneyr"
Output: 10
Explanation: 
The strings that can be formed are "hello" and "world" so the answer is 5 + 5 = 10.
'''

    def countCharacters(self, words: List[str], chars: str) -> int:
        
        res = 0
        for word in words:
            flag = 1
            for w in word:
                if word.count(w) > cahrs.count(w):
                    flag = 0
                    break
            if flag:
                res += len(word)
        return res