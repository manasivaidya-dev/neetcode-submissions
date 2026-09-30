# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diam = 0
        if not root:
            return 0
        def diameter(root):
            if not root:
                return -1 #0 when nodes, -1 when edges
            lsum = 1 + diameter(root.left)
            rsum = 1 + diameter(root.right) 
            self.diam = max(self.diam, lsum+rsum)
            return 1 + max(diameter(root.left), diameter(root.right)) 
            #returning height in terms of edges
        diameter(root)
        return self.diam
        

        