class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        while l<=r:
            mid = l+ (r-l)//2
            res= mid*mid
            if res == x:
                return mid
            if res > x:
                r=mid-1
            else: 
                l=mid+1
    
        return l-1