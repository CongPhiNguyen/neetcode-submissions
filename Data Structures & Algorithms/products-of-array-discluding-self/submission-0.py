class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        p = 1
        for i in range(len(nums) - 1):
            p*=nums[i]
            prefix.append(p)
        suffix = 1
        
        res = [1]*len(nums)
        for i in range(len(nums)):
            index = len(nums) - i - 1
            res[index] = suffix * prefix[index]
            suffix *= nums[index] 
        return res 