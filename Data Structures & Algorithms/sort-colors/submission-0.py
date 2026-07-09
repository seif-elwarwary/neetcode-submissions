class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        colors = {0:0,1:0,2:0}
        for n in nums:
            colors[n]+=1
        index = 0
        for n in range(3):
            while colors[n]:
                colors[n]-=1
                nums[index] = n
                index+=1