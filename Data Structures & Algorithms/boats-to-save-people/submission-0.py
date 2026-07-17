class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        max_w= max(people)
        counts = [0] * (max_w + 1)
        n = len(people)
        for p in people:
            counts[p]+=1
        idx,i =0,1
        while idx < n:
            while counts[i] == 0: i+=1
            people[idx] = i
            counts[i]-=1
            idx+=1
        
        res, l, r =0,0,n-1
        while l<=r:
            rem = limit - people[r]
            r-=1
            res+=1
            if l<=r and rem >= people[l]: l+=1
        return res

