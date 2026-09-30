# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        if not root.left:
            root.left = root.right
            root.right = None
            self.invertTree(root.left)
        elif not root.right:
            root.right = root.left
            root.left = None
            self.invertTree(root.right)
        if root.right and root.left:
            temp = root.right
            root.right = root.left
            root.left = temp
            self.invertTree(root.right)
            self.invertTree(root.left)
        return root
        
        