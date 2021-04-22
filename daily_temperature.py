'''
how many days you would have to wait until a warmer temperature
T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

'''
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = []
        
        for i, e in enumerate(T):
            while stack and T[stack[-1]] < e:
                cur = stack.pop()
                res[cur] = i - cur 
            stack.append(i)
        return res