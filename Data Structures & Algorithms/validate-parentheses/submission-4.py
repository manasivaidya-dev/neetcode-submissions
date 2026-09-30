from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) % 2 != 0:
            return False
        stack = deque()
        opening_to_closing = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in opening_to_closing:
                stack.append(char)
            elif char in opening_to_closing.values():
                if len(stack) == 0:
                    return False
                last_brace = stack.pop()
                if opening_to_closing[last_brace] != char:
                    return False
        if len(stack) != 0:
            return False
        return True



        