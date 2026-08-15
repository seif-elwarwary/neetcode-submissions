class Solution:
    def tribonacci(self, n: int) -> int:
        cache = {0:0,1:1,2:1}
        def fib(i):
            if i <= 2: return cache[i]
            if i in cache: return cache[i]
            cache[i] = fib(i-1) + fib(i-2) + fib(i-3)
            return cache[i]
        return fib(n)