# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append((root,0))
        answer = []
        level = []
        curr_depth = 0
        while q:
            print(q)
            node,depth = q.popleft()
            if depth == curr_depth:
                level.append(node.val)
            else:
                answer.append(level)
                level = []
                curr_depth = depth
                level.append(node.val)
            if node.left:
                q.append((node.left, depth + 1))
            if node.right:
                q.append((node.right, depth + 1))
        answer.append(level)
        return answer

        