# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        self.elems = []
        #inorder traversal
        def inorder(root):
            if not root:
                return 
            inorder(root.left)
            self.elems.append(root.val)
            inorder(root.right)
        inorder(root)
        print(self.elems)
        return self.elems[k-1]