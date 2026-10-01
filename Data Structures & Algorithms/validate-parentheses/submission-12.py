from collections import deque

class Solution:
    def isValid(self, s: str) -> bool:
        length = len(s)
        if (length % 2 )== 1 :
            return False
        
        stack = deque()
        stack.append(s[0])

        pair = {'{': '}', '[': ']', '(': ')'}


        for i in range(1, length):
            if len(stack) > 0 and stack[-1] in pair and  pair[stack[-1]] == s[i]:
                stack.pop()
            else:
                stack.append(s[i])

        return len(stack) == 0


        