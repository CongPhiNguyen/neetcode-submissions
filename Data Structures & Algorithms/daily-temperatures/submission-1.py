class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        s = []
        res = [0]* len(temperatures)
        for i, val in enumerate(temperatures):
            while s and temperatures[s[-1]] < val:
                res[s[-1]] = i - s[-1]
                s.pop()
            s.append(i)
        return res
