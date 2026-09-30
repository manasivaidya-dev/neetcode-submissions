# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = deque()
        q.append((root, 0))
        curr_level = -1
        answer = []
        while q:
            node, level = q.popleft()
            if level != curr_level:
                curr_level = level
                answer.append(node.val)
            if node.right:
                q.append((node.right, level+1))
            if node.left:
                q.append((node.left,level+1))
        return answer


        