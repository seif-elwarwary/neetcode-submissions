class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts = defaultdict(int)
        counts[0] = 1
        total = 0
        prefix = 0
        for num in nums:
            prefix += num
            total += counts[prefix - k]
            counts[prefix] += 1
        return total