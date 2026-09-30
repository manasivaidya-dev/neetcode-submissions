# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        minval = -float('inf')
        maxval = float('inf')
        def valid(root,minval,maxval):
            if not root:
                return True
            if root.left and (root.left.val <= minval or root.left.val >= root.val):
                return False
            if root.right and (root.right.val >= maxval or root.right.val <= root.val):
                return False
            return valid(root.left,minval,root.val) and valid(root.right,root.val,maxval)
        return valid(root,minval,maxval)