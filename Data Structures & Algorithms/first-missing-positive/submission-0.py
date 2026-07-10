class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n=len(nums)
        nums = [max(0,x) for x in nums]
        for i in range(n):
            val = abs(nums[i])
            if 1 <= val <= n:
                if nums[val-1] > 0:
                    nums[val-1] *= -1
                elif nums[val-1] == 0:
                    nums[val-1] = -2 * (n)
        for i in range(n):
            if nums[i]>=0:
                return i+1
        return n+1