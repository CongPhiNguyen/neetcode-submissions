class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                sum = nums[left] + nums[right] + nums[i]
                if sum < 0:
                    left += 1
                elif sum > 0:
                    right -= 1
                else:
                    res.add((nums[i], nums[left], nums[right]))
                    left += 1
                    while (
                        nums[left] == nums[left - 1] or nums[left] + nums[right] < -nums[i]
                    ) and left < right:
                        left += 1
                    while nums[left] + nums[right] > -nums[i] and left < right:
                        right -= 1
        return [list(s) for s in list(res)]