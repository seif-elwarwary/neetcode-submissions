class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total%k !=0: return False
        target = total//k
        used = [False] * len(nums)
        nums.sort(reverse=True)

        def dfs(i, k, subsum):
            if k==0: return True
            if subsum == target:
                return dfs(0,k-1,0)
            for j in range(i,len(nums)):
                if used[j] or subsum+nums[j]> target: continue
                used[j] = True
                if dfs(j+1,k,subsum+nums[j]): return True
                used[j]=False
            return False
        return dfs(0,k,0)
