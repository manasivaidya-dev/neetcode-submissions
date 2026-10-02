import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        alnum = set(string.ascii_letters + string.digits)
        left, right = 0, len(s) -1
        s=s.lower()
        while left < right:
            if s[left] not in alnum or s[left] == ' ':
                left += 1 
                continue
            elif s[right] not in alnum or s[right] == ' ':
                right -= 1
                continue
            elif s[right] != s[left]:
                #print(s[left],s[right])
                return False
            left += 1
            right -= 1
        return True
        