class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l=0
        for i in range(min(map(len, strs))):
            chars = [s[i] for s in strs]
            if all(x == chars[0] for x in chars):
                l+=1
            else:
                break
        return strs[0][:l] if l>0 else ''