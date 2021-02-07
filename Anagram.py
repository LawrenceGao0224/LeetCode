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