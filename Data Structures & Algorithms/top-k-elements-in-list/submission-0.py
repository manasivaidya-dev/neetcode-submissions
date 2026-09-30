class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_to_freq = {}
        for num in nums:
            print(num)
            if num in num_to_freq:
                num_to_freq[num] += 1
            else:
                num_to_freq[num] = 1
        output = []
        while k > 0:
            max_freq = (0,0)
            for key, val in num_to_freq.items():
                print(key, val)
                if val > max_freq[1]:
                    max_freq = (key,val)
            output.append(max_freq[0])
            del num_to_freq[max_freq[0]]
            k -= 1
        return output
                
        