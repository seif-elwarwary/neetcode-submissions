class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if sum(matchsticks) % 4 != 0:
            return False
        sides = [0]*4
        side_l = sum(matchsticks)//4
        matchsticks.sort()
        matchsticks.reverse()
        def dfs(i):
            if i ==len(matchsticks):
                return sides[0] == sides[1] == sides[2]== sides[3] == side_l
            for s in range(4):
                if sides[s] + matchsticks[i] <= side_l:
                    sides[s] +=matchsticks[i]
                    if dfs(i+1): return True
                    sides[s] -=matchsticks[i]
                if sides[s] == 0:
                    break
            return False
        return dfs(0)

            