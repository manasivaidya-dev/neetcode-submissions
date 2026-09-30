class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        freq_to_vals = [[]] * (len(nums) + 1)
        for num in nums:
            if num in num_to_freq:
                num_to_freq[num] += 1
            else:
                num_to_freq[num] = 1
        for i in range(len(nums) + 1):
            for key, val in num_to_freq.items():
                if val == i:
                    freq_to_vals[i].append(key) 
        output = []
        for i in range(len(nums), -1, -1):
            print(i, k, freq_to_vals[i])
            if k == 0:
                return output
            if len(freq_to_vals[i]) != 0:
                val = freq_to_vals[i].pop()
                output.append(val)
                k -= 1
        return output
                
        