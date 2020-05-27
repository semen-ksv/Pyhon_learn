a = [23, 435, 2, 34, 78, 35, 93, 21, 62, 42, 896, 456, 28, 5, 88, 3, 134, 4, 234, 990, 74, 12, 1]

b = [1, 2, 3, 4, 5, 12, 21, 23, 28, 34, 35, 42, 62, 74, 78, 88, 93, 134, 234, 435, 456, 896, 990]


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __repr__(self):
        return f'<Node {self.value}>'


class BinaryTree:
    def __init__(self, head: Node):
        self.head = head

    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError(f'A nod {new_node.value} already exist')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                else:
                    current_node.left = new_node
                    break
            elif new_node.value > current_node.value:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break

    def find(self, value: int):
        current_node = self.head
        while current_node:
            if value == current_node.value:
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left
        raise LookupError(f'A node with value {value} was not found.')


    def inorder(self):
        self._inorder_recursive(self.head)

    def _inorder_recursive(self, current_node):
        if not current_node:
            return
        self._inorder_recursive(current_node.left)
        print(current_node)
        self._inorder_recursive(current_node.right)

    def preorder(self):
        self._preorder_recursive(self.head)

    def _preorder_recursive(self, current_node):
        if not current_node:
            return
        print(current_node)
        self._inorder_recursive(current_node.left)
        self._inorder_recursive(current_node.right)

    def find_parent(self, value: int) -> Node:
        if self.head and self.head.value == value:
            return self.head
        current_node = self.head
        while current_node:
            if (current_node.left and current_node.left.value == value) or\
                    (current_node.right and current_node.right.value == value):
                return current_node
            elif value > current_node.value:
                current_node = current_node.right
            elif value < current_node.value:
                current_node = current_node.left



    def find_rightmost(self, node: Node) -> Node:
        current_node = node
        while current_node.right:
            current_node = current_node.right
        return current_node

    def delete(self,value: int):
        to_delete = self.find(value)
        to_delete_parent = self.find_parent(value)

        if to_delete.left and to_delete.right:
            rightmost = self.find_rightmost(to_delete.value)
            rightmost_parent = self.find_parent(rightmost.value)

            if rightmost_parent != to_delete:
                rightmost_parent.right = rightmost.left
                rightmost.left = to_delete.left
            rightmost.right = to_delete.right

            if to_delete == to_delete_parent.left:
                to_delete_parent.left = rightmost
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = rightmost
            else:
                self.head = rightmost

        elif to_delete.left or to_delete.right:
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = to_delete.right or to_delete.left
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = to_delete.right or to_delete.left
            else:
                self.head = to_delete.right or to_delete.left
        else:
            if to_delete == to_delete_parent.left:
                to_delete_parent.left = None
            elif to_delete == to_delete_parent.right:
                to_delete_parent.right = None
            else:
                self.head = None


tree = BinaryTree(Node(6))
tree.add(Node(5))
tree.add(Node(7))
tree.add(Node(3))
tree.add(Node(4))
tree.add(Node(8))
tree.add(Node(9))



print(tree.head, tree.head.left, tree.head.right, tree.head.left.value)

tree.inorder()
tree.preorder()
tree.delete(4)
tree.preorder()
# print(tree.find(21))
# print(tree.find(8))


