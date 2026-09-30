class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = set()
        max_ss = 0
        left = 0
        for i in range(len(s)):
            print(letters)
            if s[i] not in letters:
                letters.add(s[i])
            else: 
                max_ss = max(max_ss, i - left)
                while s[i] in letters:
                    letters.remove(s[left])
                    left += 1
                    print(s[left])
                letters.add(s[i])
        return max(max_ss, len(letters))
        