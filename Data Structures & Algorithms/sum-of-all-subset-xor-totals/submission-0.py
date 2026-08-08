from functools import reduce
import operator

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        total = 0
        arr = []
        def dfs(i):
            nonlocal total
            if i == len(nums): 
                total+= reduce(operator.xor, arr,0)
                return
            dfs(i+1)
            arr.append(nums[i])
            dfs(i+1)
            arr.pop()

        dfs(0)
        return total