class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for val in nums:
            if seen.get(val): 
                return True
            seen[val] = 1
        return False