class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [0] * len(nums)
        prefix[0] = 1
        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        final = [0] * len(nums)
        suffix = [0] * len(nums)
        suffix[len(nums) - 1] = 1
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
            final[i] = suffix[i]*prefix[i]
        final[len(nums) - 1] = suffix[len(nums) - 1]*prefix[len(nums) - 1]
        return final



        '''output = []
        pref_product = 1
        for num in nums:
            net_product *= num
        for i in range(len(nums)):
            if nums[i] != 0:
                number = net_product // nums[i]
                output.append(number)
            else:
                product = 1
                for j in range(len(nums)):
                    print(product)
                    if j != i:
                        product *= nums[j]
                output.append(product)
        return output'''

        
        