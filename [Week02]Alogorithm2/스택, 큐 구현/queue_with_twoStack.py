class Queue:

    def __init__(self):
        self._stack1 = []
        self._stack2 = []

    def __len__(self):
        return len(self._stack1) + len(self._stack2)

    def enQueue(self, data):
        self._stack1.append(data)

    def deQueue(self):
        if len(self._stack2) == 0:
            while len(self._stack1) != 0:
                self._stack2.append(self._stack1.pop())

        return self._stack2.pop()
