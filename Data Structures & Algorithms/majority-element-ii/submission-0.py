class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counts = defaultdict(int)
        output = set()
        ln = (len(nums) //3 )+ 1
        for n in nums:
            counts[n]+=1
            if counts[n] == ln:
                output.add(n)
        return list(output)