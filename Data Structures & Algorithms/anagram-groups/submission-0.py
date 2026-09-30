class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_to_strs = {}
        #output = []
        for string in strs:
            sorted_string = sorted(string)
            joined_string = ''.join(sorted_string)
            print(joined_string)
            if joined_string in sorted_to_strs:
                sorted_to_strs[joined_string].append(string)
            else:
                sorted_to_strs[joined_string] = []
                sorted_to_strs[joined_string].append(string)
        output_copy = [l.copy() for l in sorted_to_strs.values()]
        return output_copy
        