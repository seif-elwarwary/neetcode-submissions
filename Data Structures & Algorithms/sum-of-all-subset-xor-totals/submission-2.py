from _operator import le
from functools import reduce
import operator

class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        r=0
        for n in nums:
           r|=n 
        return  r << (len(nums)-1)