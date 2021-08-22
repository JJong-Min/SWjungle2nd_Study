class Stack:

    def __init__(self):
        self._queue1 = []
        self._queue2 = []

    def __len__(self):
        return len(self._queue1)

    def push(self, data):
        if len(self._queue1) == 0:
            self._queue1.append(data)

        else:
            while len(self._queue1) != 0:
                self._queue2.append(self._queue1.pop(0))

            self._queue1.append(data)

            while len(self._queue2) != 0:
                self._queue1.append(self._queue2.pop(0))

    def pop(self):
        return self._queue1.pop(0)
