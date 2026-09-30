class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_num = set("abcdefghijklmnopqrstuvwxyz1234567890")
        s = s.lower()
        left = 0
        right = len(s) -1
        while left < right:
            print(left, right)
            while left < right and s[left] not in alpha_num:
                left += 1
            while left < right and s[right] not in alpha_num:
                right -= 1
            if s[left] != s[right]:
                return False  
            left += 1
            right -= 1 
        return True
        