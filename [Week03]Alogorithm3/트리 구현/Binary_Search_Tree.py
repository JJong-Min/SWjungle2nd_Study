import random

class Node:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.data)

class SearchTree:
    def __init__(self):
        self.root = None

    def insertElement(slef, data):
        new_node = Node(data)
        if self.root == None:
            self.root = new_node

        node = self.root
        while True:
            prev_node = node
            if node.data < new_node.data:
                node = node.left
                if node == None:
                    node = new_node
                    prev_node.left = node
            elif node.data < new_node.data:
                node = node.right
                if node == None:
                    node = new_node
                    prev_node.right = node
            else:
                return


    def searchElement(self, data):
        node = self.root
        while True:
            if node.data > data:
                node = node.left
            elif node.data < data:
                node = node.right
            elif node.data == data:
                break
            else:
                return Node("탐색 결과 없음")

        return node

    def preorderTraversal(self, node):
        print(node, end='')
        if not node.left == None:
            self.preorderTraversal(node.left)
        if not node.right == None:
            self.preorderTraversal(node.right)

    def inorderTraversal(self, node):
        if not node.left == None:
            self.preorderTraversal(node.left)
        print(node, end='')
        if not node.right == None:
            self.preorderTraversal(node.right)

    def postorderTraversal(self, node):
        if not node.left == None:
            self.preorderTraversal(node.left)
        if not node.right == None:
            self.preorderTraversal(node.right)
        print(node, end='')

    def removeElement(self, data):
        node = self.root
        parent = None
        is_left_child = True
        while True:
            if node is None:
                return False

            if data == node.data:
                break

            else:
                parent = node
                if data < node.data:
                    is_left_child = True
                    node = node.left
                else:
                    is_left_child = False
                    node = node.right

        if node.left is None:
            if node is self.root:
                self.root = node.right

            elif is_left_child:
                parent.left = node.right

            else:
                parent.right = node.right

        else:
            parent = node
            left = node.left
            is_left_child = True
            while left.right is not None:
                parent = left
                left = left.right
                is_left_child = False

            node.data = left.data
            node
        
        
