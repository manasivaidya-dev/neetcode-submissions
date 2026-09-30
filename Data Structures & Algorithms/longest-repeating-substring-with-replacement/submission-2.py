class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char_set = set(s)
        ss_len = 0

        for c in char_set:
            c_count = 0
            right, left = 0, 0
            while right < len(s):
                if s[right] == c:
                    c_count += 1
                    ss_len = max(ss_len, right - left + 1)
                    right += 1
                else:
                    if (right - left + 1) - c_count <= k:
                        ss_len = max(ss_len, right - left + 1)
                        right += 1
                    else:
                        while (right - left + 1) - c_count > k:
                            if  s[left] == c:
                                c_count -= 1
                            left += 1
                        ss_len = max(ss_len, right - left + 1)
        return ss_len




        

        