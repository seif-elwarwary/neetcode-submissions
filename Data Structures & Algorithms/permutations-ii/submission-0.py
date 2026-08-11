class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        n = len(nums)
        def dfs(perm):
            if len(perm)==n:
                res.add(tuple(perm))
                return
            for i in range(n):
                if nums[i] != -100:
                    perm.append(nums[i])
                    nums[i] = -100
                    dfs(perm)
                    nums[i] = perm.pop()
        dfs([])
        return list(res)