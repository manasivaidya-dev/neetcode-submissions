class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters = {}
        if len(s) != len(t):
            return False
        for letter in s:
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
        for letter in t:
            if letter in letters:
                print(letter,letters[letter])
                letters[letter] -= 1
                if letters[letter] == -1:
                    return False
            else:
                return False
        return True
        