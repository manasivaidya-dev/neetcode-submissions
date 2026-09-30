# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.curr_max = -101
        self.good_nodes = 0
        def good(root, curr_max):
            if not root:
                return 0
            if root.val >= curr_max:
                curr_max = root.val
                self.good_nodes += 1
            left = good(root.left, curr_max)
            right = good(root.right, curr_max)
        
        good(root, root.val)
        return self.good_nodes



        