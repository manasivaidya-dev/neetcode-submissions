class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = []
        net_product = 1
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
        return output

        
        