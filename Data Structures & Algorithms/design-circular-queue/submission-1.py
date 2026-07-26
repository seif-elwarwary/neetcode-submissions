class MyCircularQueue:

    def __init__(self, k: int):
        self.cap = k
        self.size = 0
        self.data = [0]*k
        self.front = 0
        self.rear = 0
    def enQueue(self, value: int) -> bool:
        if self.size  == self.cap : return False
        self.size+=1
        self.data[self.rear] = value
        self.rear +=1
        self.rear=self.rear%self.cap
        return True

    def deQueue(self) -> bool:
        if self.size == 0 : return False
        self.size-=1
        self.front +=1
        self.front= self.front%self.cap
        return True

    def Front(self) -> int:
        if self.size == 0 : return -1
        return self.data[self.front]

    def Rear(self) -> int:
        if self.size == 0 : return -1
        return self.data[(self.rear-1)%self.cap]
        

    def isEmpty(self) -> bool:
        return self.size == 0

    def isFull(self) -> bool:
        return self.size == self.cap
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()