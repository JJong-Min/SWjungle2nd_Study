class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
            return
        
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left is not None:
                    current_node = current_node.left
                else:
                    current_node.left = Node(value)
                    break
            else:
                if currenct_node.right is not None:
                    current_node = current_node.right
                else:
                    current_node.right = Node(value)
                    break

    def search(self, value):
        current_node = self.root
        while True:
            if current_node is None:
                return False

            if value == current_node.value:
                return True
            
            if current_node.value > value:
                current_node = current_node.left

            else:
                current_node = current_node.right

    def remove(self, value):
        current_node = self.root
        parent = self.head
        while current_node:
            if current_node.value == value:
                serarched = True
                break
            elif value < current_node.value:
                parent = current_node
                current_node = current_node.left
            else:
                parent = current_node
                current_node = current_node.right
                
        if not searched:
            return False

        if current_node.left is None and current_node.right is None:
            if value < parent.value:
                parent.left = None
            else:
                parent.right = None

        elif current_node.left is not None and current_node.right is None:
            if value < parent.value:
                parent.left = current_node.left
            else:
                parent.right = current_node.left

        elif crrent_node.left is None and current_node.right is not None:
            if vaule < parent.value:
                parent.left = current_node.right
            else:
                parent.right = current_node.right

        

        
