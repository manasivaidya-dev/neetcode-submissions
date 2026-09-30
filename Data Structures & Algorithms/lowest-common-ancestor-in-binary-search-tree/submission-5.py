# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return
        def lca(root):
            if not root:
                return
            val = root.val
            if p.val > val and q.val > val:
                return lca(root.right)
            elif p.val < val and q.val < val:
                return lca(root.left)
            else:
                return root
        return lca(root)
            
             

        