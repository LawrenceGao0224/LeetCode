
'''
House robber 3
Input: root = [3,2,3,null,3,null,1]
Output: 7
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.
'''


class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        def superrob(root):
            if not root: return (0, 0)

            left, right = superrob(root.left), superrob(root.right)
            
            now = root.val + left[1] + right[1]
            
            later = max(left) + max(right)
            
            return (now, later)
        
        return max(superrob(root))
        
  