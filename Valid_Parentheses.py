# 20. Valid Parentheses
class Solution(object):
    def isValid(self, s):
        group = { 
            '(' : ')' ,
            '{' : '}', 
            '[' : ']'
        }
        stack = []

        for e in s:
            if e in group.keys():
                stack.append(e)
            elif e in group.values():
                if not stack:
                    return False
                a = stack.pop()
                if group[a] == e:
                    continue
                else:
                    return False
        return len(stack) == 0 