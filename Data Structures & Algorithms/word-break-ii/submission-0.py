class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        def dfs(i):
            if i == len(s):
                res.append(' '.join(curr))
                return
            for j in range(i,len(s)):
                word = s[i:j+1]
                if word in words:
                    curr.append(word)
                    dfs(j+1)
                    curr.pop()

        res=[]
        curr=[]
        dfs(0)
        return res