#쓰레드 이진 트리
class Node:
    def __init__(self, data):
        self.data  = data
        self.left = None
        self.right = None
        self.is_thread_right = None

    def __str__(self):
        return str(self.data)

class ThreadTree:
    def __init__(self):
        self.root = None

    def inorderTraversal(self, node):
        while not node.left = None:
            node = node.left
        print(node, end='')
        while True:
            node = self.findThread(node)
            print(node, end(''))
            if node.right == None:
                break

    def findThread(self, node):
        pre_node = node
        node = node.reight
        if node == None or pre_node.is_thread_right:
            return node
        while not node.left == Node:
            node = node.left
        return node

    def makeRoot(self, node, lleft_node, right_node, thread):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node
        node.is_thread_right = thread
