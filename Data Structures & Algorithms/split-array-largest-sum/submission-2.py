class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(target):
            j=0
            for i in range(k):
                t=0;
                while j<n and (t+nums[j])<=target:
                    t+=nums[j]
                    j+=1
            return j==n
        n = len(nums)
        l=max(nums); r= sum(nums)
        res = r
        while l<=r:
            m=(l+r)//2
            if canSplit(m):
                res = min(res,m)
                r=m-1
            else: l+=1
        return res