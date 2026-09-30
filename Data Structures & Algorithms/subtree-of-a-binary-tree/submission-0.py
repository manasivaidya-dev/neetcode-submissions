# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def issameTree(self,p: Optional[TreeNode], q:Optional[TreeNode]) -> bool:
        if (p and not q) or (q and not p):
            return False
        if not p and not q:
            return True
        if p.val != q.val:
            return False
        left = self.issameTree(p.left, q.left)
        right = self.issameTree(p.right, q.right)

        if not left or not right:
            return False
        else:
            return True
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if not subRoot:
            return True
        same_root = self.issameTree(root, subRoot)
        same_left = self.isSubtree(root.left, subRoot)
        same_right = self.isSubtree(root.right, subRoot)

        if same_root or same_left or same_right:
            return True
        else:
            return False
            
        


        