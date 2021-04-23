'''
Input: root = [1,2,3,null,5,null,4]
Output: [1,3,4]
'''
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        def visit(node, depth):
            if node:
                if len(view) == depth:
                    view.append(node.val)
                visit(node.right, depth + 1)
                visit(node.left, depth + 1)

        view = []
        visit(root, 0)
        return view    