class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        ks= set()
        L = 0
        for R in range(len(nums)):
            if R-L>k:
                ks.remove(nums[L])
                L+=1
            if nums[R] in ks:
                return True
            ks.add(nums[R])
        return False
