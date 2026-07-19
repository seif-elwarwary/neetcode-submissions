class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n = len(nums)
        l,r =0,n
        while l< r:
            mid = l+(r-l)//2
            if nums[mid] >=target:
                r = mid
            else:
                l=mid+1
        return l