# 39. Combination Sum
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        dp = [[]for i in range(target + 1)]
        for c in candidates:
            for i in range(1, target+1):
                if c > i :
                    continue
                elif c == i:
                    dp[i].append([c])
                else:
                    for j in dp[i-c]:
                        dp[i].append(j +[c])
        return dp[target]