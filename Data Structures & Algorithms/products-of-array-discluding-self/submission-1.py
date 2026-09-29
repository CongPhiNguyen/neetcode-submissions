class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]
        p = 1
        for i in range(len(nums) - 1):
            p*=nums[i]
            res.append(p)
        suffix = 1
        
        for i in range(len(nums)):
            index = len(nums) - i - 1
            res[index] *= suffix
            suffix *= nums[index] 
        return res 