class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        l=1; r=n-2
        while l<=r:
            m= (r+l)//2
            left,mid,right = mountainArr.get(m-1),mountainArr.get(m),mountainArr.get(m+1)
            if left>mid>right:
                r=m-1
            elif left<mid<right:
                l=m+1
            else: break
        peak = m
        l=0
        r=peak-1
        while l<=r:
            m= (r+l)//2
            mid= mountainArr.get(m)
            if mid > target:
                r=m-1
            elif mid< target:
                l=m+1
            else:
                return m
        
        l=peak
        r=n-1
        while l<=r:
            m= (r+l)//2
            mid= mountainArr.get(m)
            if mid < target:
                r=m-1
            elif mid> target:
                l=m+1
            else:
                return m
        return -1
        