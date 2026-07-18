class FreqStack:

    def __init__(self):
        self.cnt = defaultdict(int)
        self.stacks = defaultdict(list)
        self.max_cnt = 0

    def push(self, val: int) -> None:
        self.cnt[val]+=1
        self.stacks[self.cnt[val]].append(val)
        self.max_cnt = max(self.max_cnt, self.cnt[val])

    def pop(self) -> int:
        val = self.stacks[self.max_cnt].pop()
        if len(self.stacks[self.max_cnt]) == 0:
            self.max_cnt-=1
        self.cnt[val]-=1
        return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()