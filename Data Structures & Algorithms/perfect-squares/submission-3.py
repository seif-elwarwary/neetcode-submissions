class Solution:
    def numSquares(self, n: int) -> int:
        dp = [n]*(n+1)
        dp[0]=0
        for i in range(1,len(dp)):
            for s in range(1,len(dp)):
                if s*s>i: break
                dp[i]=min(dp[i],1+dp[i-s*s])
            
        return dp[n]