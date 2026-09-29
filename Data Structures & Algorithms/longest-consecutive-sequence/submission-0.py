class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set()
        m = 0
        for num in nums:
            s.add(num)
        for c in s:
            if c-1 not in s:
                count = 1
                while c+count in s:
                    count+=1
                m = max(m, count)
        return m