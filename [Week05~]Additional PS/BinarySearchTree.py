class Node:
    def __init__(self, value):
        self.value = value
        self.left, self.right = None, None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def search(self, key):
        p = self.root

        while True:
            if p is None:
                return None
            if key == p.value:
                return p.value

            elif key < p.value:
                p = p.left

            else:
                p = p.right

    def insert(self, key):

        def insert_node(node, key):
            if node.value == key:
                return False

            if node.value > key:
                if node.left is None:
                    node.left = Node(key)
                else:
                    insert_node(node.left, key)

            else:
                if node.right is None:
                    node.right = Node(key)
                else:
                    insert_node(node.right, key)
            return True

        if self.root is None:
            self.root = Node(key)
        else:
            insert_node(self.root, key)

    def delete(self, value):
        if self.head is None:
            return False

        node = self.head
        parent = self.head
        check = False

        while node:
            if value == node.value:
                check = True
                break
            elif value < node.value:
                parent = node
                node = node.left
            else:
                parent = node
                node = node.right

        if not check:
            return False

        # Case1 No Child
        if node.left is None and node.right is None:
            if value < parent.value:
                parent.left = None
            else:
                parent.right = None

        # Case2 Have a One Child
        elif node.left and node.right is None:
            if value < parent.value:
                parent.left = node.left
            else:
                parent.right = node.left

        elif node.left is None and node.right:
            if value < parent.value:
                parent.left = node.right
            else:
                parent.right = node.right

        # Case3 Have Two Child
        elif node.left and node.right:
            current, child = node, node.right

            while child.left:
                current, child = child, child.left

            node.value = child.value

            if current != node:
                if child.right:
                    current.left = child.right
                else:
                    current.left = None
            else:
                node.right = child.right
        

    def pre_order_traversal(self):
        def _pre_order_traversal(root):
            if root is None:
                pass
            else:
                
                _pre_order_traversal(root.left)
                print(root.value)
                _pre_order_traversal(root.right)
        _pre_order_traversal(self.root)

    

binary_tree = BinarySearchTree()
binary_tree.insert(30)
binary_tree.insert(20)
binary_tree.insert(10)
binary_tree.insert(50)
binary_tree.insert(40)
binary_tree.pre_order_traversal()
