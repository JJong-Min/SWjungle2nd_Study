# 크기가 정해진 stack구현
class Fixedstack:
    def __init__(self, capacity):
        self.stk = [None] * capacity
        self.ptr = 0
        self.capacity = capacity

    def __len__(self):
        return self.ptr

    def isEmpty(self):
        return self.ptr <= 0

    def isFull(self):
        return self.ptr >= self.capacity

    def push(self, value):
        if self.isFull():
            return 0
        self.stk[self.ptr] = value
        self.ptr += 1

    def pop(self):
        if self.isEmpty():
            return 0
        self.ptr -= 1
        return self.stk[self.ptr]

    def peek(self):
        if self.isEmpty():
            return 0
        return self.stk[self.ptr - 1]

    def find(self, value):
        for i in range(self.ptr - 1, -1, -1):
            if self.stk[i] == value:
                return i
        return -1
