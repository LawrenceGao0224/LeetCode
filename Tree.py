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
        
