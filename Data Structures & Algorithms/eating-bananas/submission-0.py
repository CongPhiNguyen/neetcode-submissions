class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        total = sum(piles)
        l = math.ceil(total/h)
        r = max(piles)

        valid = -1
        while l <= r:
            mid = (l + r)//2
            t = sum([math.ceil(p/mid) for p in piles])
            if t > h:
                l = mid + 1
            elif t <= h:
                valid = mid
                r = mid - 1
        return valid



            


