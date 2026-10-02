class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        s = []
        max_area = 0
        
        n = len(heights)

        for i in range(n):
            while s and heights[s[-1]] > heights[i]:
                val = s.pop()
                w = 1
                if s:
                    w = i - s[-1] - 1
                else:
                    w = i
                max_area = max(max_area, w* heights[val])
            s.append(i)


        # Thing left on the stack
        while s:
            val = s.pop()
            w = 1
            if s:
                w = n - s[-1] - 1
            else:
                w = n
            max_area = max(max_area, heights[val]* w)
        return max_area