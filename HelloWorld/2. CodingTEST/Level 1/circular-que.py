# 원형 큐 디자인
# https://leetcode.com/problems/design-circular-queue/
# page.259


class MyCircularQueue:
    def __init__(self, k: int):
        self.front = 0
        self.rear = 0
        self.q = [None] * k
        self.maxlen = k

    def enQueue(self, value: int) -> bool:
        if self.q[self.rear] is None:
            self.q[self.rear] = value
            self.rear = (self.rear + 1) % self.maxlen
            return True
        else:
            return False

    def deQueue(self) -> bool:
        if self.q[self.front] is not None:
            self.q[self.front] = None
            self.front = (self.front + 1) % self.maxlen
            return True
        else:
            return False


    def Front(self) -> int:

        if self.q[self.front] is not None:
            return self.q[self.front]

        else:
            return -1
    def Rear(self) -> int:
        if self.q[ (self.rear + self.maxlen-1) % self.maxlen ] is not None:
            return self.q[ (self.rear + self.maxlen-1) % self.maxlen ]
        else:
            return -1
    def isEmpty(self) -> bool:
        if self.front == self.rear and self.q[self.front] is None:
            return True
        else:
            return False
    def isFull(self) -> bool:
        if self.front == self.rear and self.q[self.front] is not None:
            return True
        else:
            return False
