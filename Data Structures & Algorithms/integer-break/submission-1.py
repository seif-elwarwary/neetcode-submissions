class Solution:
    def integerBreak(self, n: int) -> int:
        if n<=3: return n-1
        res = 3**(n//3)
        if n%3==1:
            return 4*(res//3)
        return res*max(1,n%3)