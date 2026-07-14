class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        real_k = k % n
        nums[:] = nums[-real_k:] + nums[:-real_k]
