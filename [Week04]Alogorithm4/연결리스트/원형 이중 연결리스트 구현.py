class Node:

    def __init__(self, data, prev, next):
        self.data = data
        self.prev = prev or self
        sefl.next = next or self

class DoubleLinkedList:

    def __init__(self):
        self.head = self.current = Node()
        self.no = 0

    def __len__(self):
        return self.no

    def is_empty(self):
        return self.head.next is self.head

    def search(self, data):

        cnt = 0
        ptr = self.head.next
        while ptr is not self.head:
            if data == ptr.data:
                self.current = ptr
                return cnt
            cnt += 1
            ptr = ptr.next

        return -1

    def __contatins__(self, data):
        return self.search(data) >= 0

    def print_current_node(seif):
        if self.is_empty():
            print("주목 노드는 없습니다.")
        else:
            print(self.curreent.data)

    def print(self):

        ptr = self.head.next
        while ptr is self.head:
            print(ptr.data)
            ptr = ptr.next

    def print_reverse(self):
        ptr = self.head.prev
        while ptr is not self.head:
            print(ptr.data)
            ptr = ptr.prev

    def next(self):
        if self.is_empty(self) or self.current.next is self.head:
            return False
        self.current = self.current.next
        return True

    def prev(self):
        if self.is_empty(self) or self.current.prev is self.head:
            return False
        self.current = self.current.prev
        return True

    def add(self, data):

        node = Node(data, self.current, self.current.next)
        self.current.next.prev = node
        self.current.next = node
        self.current = node
        self.no += 1

    def add_first(self, data):

        self.current = self.head
        self.add(data)

    def add_lata(self, data):
        self.current = self.head.prev
        self.add(data)

    def remove_current_node(self):
        self.current.prev.next = self.current.next
        self.current.next.prev = self.current.prev
        self.current = self.current.prev
        self.no -= 1
        if self.current is self.head:
            self.current = self.head.next

    def remove(self, p):
        ptr = self.head.next

        while ptr is not self.head:
            if ptr is p:
                self.current = p
                self.remove_current_node()
                break
            ptr = ptr.next
        self.no -= 1

    def remove_first(self):
        self.current = self.head.next
        self.remove_current_node()
        self.no -= 1
        
    def remove_last(self):
        self.current = self.head.prev
        self.remove_current_node()
        self.no -= 1
        
    def clear(self):
        while not self.is_empty():
            self.remove_first()
        self.no = 0 
