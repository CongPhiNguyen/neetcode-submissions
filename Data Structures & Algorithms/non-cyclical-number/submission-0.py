class Solution:
    def sum_square(self, num: int) -> int:
        s = 0
        while num > 0:
            s += (num%10)**2
            num //=10
        return s
    def isHappy(self, n: int) -> bool:
        seen = set()
        s = n;
        while True:
            s = self.sum_square(s)
            if s == 1:
                return True
            if s in seen:
                return False
            seen.add(s)
        return False