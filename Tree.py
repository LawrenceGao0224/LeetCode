# 226. Invert Binary Tree
class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root

# ---------------------------------------------------------------------------------------------------------

# 100. Same Tree

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def same( pnode, qnode):    
            if not pnode and not qnode:
                return True
            elif not pnode or not qnode or pnode.val != qnode.val:
                return False
            else:
                return same(pnode.left, qnode.left) and same(pnode.right, qnode.right)
        return same(p, q) 

# ---------------------------------------------------------------------------------------------------------

# 98. Validate Binary Search Tree

    def isValidBST(self, root: TreeNode) -> bool:
        Traversal = []
        def LDR(Tree: TreeNode) -> TreeNode:
            if root:
                LDR(Tree.left)
                Traversal.append(Tree.val)
                LDR(Tree.right)
        
        LDR(root)
        if len(Traversal) == 2 and Traversal[0] >= Traversal[1]:
            return False
        for i in range(1, len(Traversal)):
            if Traversal[i-1] >= Traversal[i]:
                return False
            else:
                continue
        return True

# ----------------------------------------------------------------------------------------------------

# 104. Maximum Depth of Binary Tree

    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        max_depth = 0
        queue = [root]
        queue_next = []
        while queue:
            for root in queue:
                if root.left:
                    queue_next.append(root.left)
                if root.right:
                    queue_next.append(root.right)
            max_depth += 1
            queue = queue_next
            queue_next = []
        return max_depth

    # Recursive:
    def maxDepth2(self, root: TreeNode) -> int:
        count = 0
        def Recursive(root: TreeNode):
            if not root:
                return 0
            else:
                count = 1 + max(Recursive(root.left), Recursive(root.right))
                return count
        return Recursive(root)
#================================================================================================================
# 111. Minimum Depth of Binary Tree
"""
Input: root = [3,9,20,null,null,15,7]
Output: 2
Example 2:

Input: root = [2,null,3,null,4,null,5,null,6]
Output: 5
"""
    def minDepth(self, root: TreeNode) -> int:
        ## BFS
        if not root: return 0
        count = 1
        queue = deque([root])
        while queue:
            for i in range(len(queue)):
                node = queue.popleft()
                if not node: 
                    continue
                elif not (node.left or node.right):
                    return count
                else:
                    queue.append(node.left)
                    queue.append(node.right)
            count += 1
        return count
    
    
        ## dfs
        def dfs(root):
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if left == 0: return right+1
            if right == 0: return left+1
            return min(left,right)+1
        return dfs(root)

#================================================================================================================
# 617. Merge Two Binary Trees
"""
Input: root1 = [1,3,2,5], root2 = [2,1,3,null,4,null,7]
Output: [3,4,5,5,4,null,7]
Example 2:

Input: root1 = [1], root2 = [1,2]
Output: [2,2]
"""
    def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
        if not root1:
            return root2
        elif not root2:
            return root1
        else:
            return TreeNode(root1.val + root2.val, 
                            left = self.mergeTrees(root1.left, root2.left),
                            right = self.mergeTrees(root1.right, root2.right))




#================================================================================================================

# 230. Kth Smallest Element in a BST

    def kthSmallest(self, root: TreeNode, k: int) -> int:
        Traversal = []
        def LDR(Tree: TreeNode):
            LDR(Tree.left)
            if len(Traversal) == k:
                return
            Traversal.append(Tree.val)
            LDR(Tree.right)
        LDR(root)
        return Traversal[-1]
        
#=================================================================================================================

#105. Construct Binary Tree from Preorder and Inorder Traversal

    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        mapping = {}
        
        for i, e in enumerate(inorder):
            mapping[e] = i
        
        def construction(left, right):
            if left > right:
                return
            root = TreeNode(preorder.pop(0))
            mid = mapping[root.val]
            root.left = construction(left, mid-1)
            root.right = construction(mid+1, right)
            return root
        return construction(0, len(preorder) -1)

#==============================================================================================================
# 235. Lowest Common Ancestor of a Binary Search Tree

        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
            if not root:
                return None
            if root.val < p.val and root.val < q.val:
                return self.lowestCommonAncestor(root.right, p, q)
            if root.val > p.val and root.val > q.val:
                return self.lowestCommonAncestor(root.left, p, q)
            return root

#==============================================================================================================

# 236. Lowest Common Ancestor of a Binary Tree

        def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

            def lca(root, p, q)
                if not root:
                    return None
                if root == p or root == q:
                    return root
                
                left = lca(root.left, p, q)
                right = lca(root.right, p, q)

                if left and right :
                    return root
                else:
                    if left:
                        return left
                    else:
                        return right
            lca(root, p, q)

#==============================================================================================================
# 124. Binary Tree Maximum Path Sum

    def maxPathSum(self, root: TreeNode) -> int:

        self.maxsum = float('-inf')
        
        def DFS(root):
            if not root: return 0
            left = DFS(root.left)
            right = DFS(root.right)

            all_path = root.val + left + right
            left_path = root.val + left
            right_path = root.val + right

            self.maxsum = max(self.maxsum, root.val, all_path, left_path, right_path) 

            return max(left_path, right_path, root.val)

        DFS(root)
        return self.maxsum

#==============================================================================================================
# def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

"""
Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted:

Input: nums = [1,3]
Output: [3,1]
Explanation: [1,3] and [3,1] are both a height-balanced BSTs.
"""

    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0])
        def BST(nums, left, right):
            if left > right:
                return None
            mid = (left+right) // 2
            left = BST(nums, left, mid-1)
            right = BST(nums, mid+1, right)
            return TreeNode(nums[mid], left, right)
        return BST(nums, 0, len(nums)-1)


#==============================================================================================================
# 112. Path Sum
'''
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
'''
    #BFS
    def hasPathSum(self, root: TreeNode, targetSum: int) -> bool:
        
        if not root:
                return False
        
        queue = deque()
        queue.append((root, targetSum - root.val))
        
        while queue:
            node, current = queue.popleft()
            if not node.left and not node.right and current == 0:
                return True
            if node.left:
                queue.append((node.left, current - node.left.val))
            if node.right:
                queue.append((node.right, current - node.right.val))
                
        return False
     