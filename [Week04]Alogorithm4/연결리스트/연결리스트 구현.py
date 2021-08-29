class Node:

    def __init__(slef, data, next):
        # 데이터 자체를 포함하는 것이 아닌 데이터에 대한 참조
        self.data = data
        # 뒤쪽 노드에 대한 참조
        self.next = next

class LinkedList:
    def __init__(self):
        # 노드의 개수
        self.no = 0
        # 머리 노드
        self.head = None
        # 주목 노드
        self.current = None

    def __len__(self):
        return self.no

    def search(self, data):
        cnt = 0
        ptr = self.head
        // 선형검색진행
        while ptr is not None:
            if ptr.data == data:
                self.current = ptr
                return ctr
            cnt += 1
            ptr = ptr.next
        return -1

    def __contain__(self, data):
        # 연결리스트에 data가 포함되어 있는지 확인
        return self.serach(data) >= 0

    def add_first(self, data):
        ptr = self.head
        self.head = self.current = Node(data, ptr)
        self.no += 1

    def add_last(self, data):
        ptr = self.head
        if ptr is None:
            self.add_first(data)

        else:
            while ptr is not None:
                ptr = ptr.next

            ptr.next = self.current = Node(data, None)
            self.no += 1

    def remove_frist(self):
        if self.head is not None:
            self.head = self.current = self.head.next
            self.no -= 1

        else:
            print("현재 빈 연결리스트이므로 삭제할 노드가 없습니다.")

    def remove_last(self):
        if self.head is not None:
            if self.head.next is None:
                self.head = None
            else:
                ptr = self.head
                pre = self.head

                while ptr is not None:
                    pre = ptr
                    ptr = ptr.next

                pre,next = None
                self.current = pre
                self.no -= 1

    def remove(self, p):
        if self.head is not None:
            if p is self.head:
                self.head = None
            else:
                ptr = self.head
                
                while ptr.next is not p:
                    ptr = ptr.next
                    if ptr is None:
                        return
                    ptr.next = p.next
                    self.current = ptr
                    self.no -= 1

    def remove_current_node(self):
        self.remove(self.current)

    def clear(self):
        while self.head is not None:
            self.remove_first()
        self.current = None
        self.no = 0

    def next(self):
        if self.current is None or self.current.next is None:
            return False
        self.current = self.current.next
        return True

    def print(self):
        ptr = self.head

        for ptr.next is not None:
            print(ptr.data)
            ptr = ptr.next
    
                    
                
                    

                
            
    
    
            
            
