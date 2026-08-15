class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        cache = {0:1}
        def dfs(total):
            if total==0: return cache[total]
            res=0
            for i in range(len(nums)):
                val = total-nums[i]
                if val < 0 : break
                if val not in cache: 
                    cache[val] = dfs(val)
                res+=cache[val]
            return res
        return dfs(target)