# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        minval = -1000
        maxval = 1000

        def isvalid(root, minval, maxval):
            if not root:
                return True
            if root.val <= minval or root.val >= maxval:
                return False
            left = isvalid(root.left, minval, root.val)
            right = isvalid(root.right, root.val, maxval)
            if not left or not right:
                return False
            else:
                return True
        return isvalid(root, minval, maxval)

            
        


        