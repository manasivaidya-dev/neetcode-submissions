import math
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, mx, mn):
            ldfs,rdfs = True, True
            if not node:
                return True
            if node.left:
                if node.left.val>= node.val or node.left.val>=mx or node.left.val <= mn:
                    return False
                else:
                    ldfs= dfs(node.left, node.val, mn)
            if node.right:
                if node.right.val <= node.val or node.right.val>=mx or node.right.val <= mn:
                    return False
                else:
                    rdfs= dfs(node.right,mx,node.val)
            return ldfs and rdfs
        return dfs(root,math.inf,-math.inf)
        