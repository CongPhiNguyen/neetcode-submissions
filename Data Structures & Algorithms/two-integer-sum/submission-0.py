class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_s = {}
        for i, val in enumerate(nums):
            if hash_s.get(target - val, -1) != -1:
                return [ hash_s.get(target - val), i ]
            hash_s[val] = i
        return []