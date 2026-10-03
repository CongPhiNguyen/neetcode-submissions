class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = 1
        m = abs(n)
        base = x
        while m > 0:
            if m%2==1: 
                exp*=base

            base*=base
            m //= 2
        return exp if n > 0 else 1/(exp) 