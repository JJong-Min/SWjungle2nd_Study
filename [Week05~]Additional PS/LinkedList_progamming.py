class Node(self, data, next):
    def __init__(self, data, next):
    self.data = data
    self.next = next

class LinkedList:
    def __init__(self):
        self.no = 0
        self.head = None
        self.current = None

    def __len__(self):
        return self.no

    def search(self, data):
        ptr = self.head
        cnt = 0
        while ptr is not None:
            if ptr.data == data:
                return cnt
            cnt += 1
            ptr = ptr.next

        return -1

    def add_first(self, data):
        ptr = self.head
        self.head = Node(data, ptr)
        self.no += 1

    def add_last(self, data):
        if self.head is None:
            add_first(data)

        else:
            ptr = self.head
            while ptr.next is not None:
                ptr = ptr.next
            ptr.next = Node(data, None)
            self.no += 1

    def remove_first(self):
        if self.head is not None:
            self.head = self.head.next
            self.no -=1

    def remove_last(self):
        if self.head is not None:
            if self.head.next is None:
                remove_first()
            else:
                ptr = self.head
                pte = self.head

                while ptr.next is not None:
                    pre = ptr
                    ptr = ptr.next

                pre.next = None
                self.current = pre
                self.no -= 1
            
