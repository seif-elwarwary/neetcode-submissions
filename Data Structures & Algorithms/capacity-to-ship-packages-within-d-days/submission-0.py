class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = max(weights)
        r = sum(weights)
        res = r
        def canShip(cap):
            ships = 1
            currCap = cap
            for w in weights:
                if currCap - w<0:
                    ships+=1
                    if ships> days:
                        return False
                    currCap =cap
                currCap-=w
            return True
        while l<=r:
            m = (l+r)//2
            if canShip(m):
                res = min(res, m)
                r=m-1
            else:
                l=m+1
        return res