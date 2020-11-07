from collections import deque
from typing import List, Any


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class BST:
    __TRAVERSAL_TYPES = ["in_order", "pre_order", "post_order"]

    def __init__(self, root: Node = None):
        self.root = root

    def __str__(self):
        output = ""
        queue = deque()
        queue.append(self.root)
        while len(queue) > 0:
            n = len(queue)
            level = []
            for i in range(n):
                current = queue.popleft()
                level.append(current.value)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            output += str(level) + "\n"

        return output.rstrip("\n")

    def insert(self, value) -> None:
        if not self.root:
            self.root = Node(value)
            return None

        current_node = self.root
        new_node = Node(value)
        while True:
            if new_node.value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    return None
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    return None
                current_node = current_node.right

    def remove(self, value) -> None:
        self.__delete_node(self.root, value)

    def __delete_node(self, node, value):
        # Base Case
        if node is None:
            return node
        # If the value to be deleted is smaller than the node's
        # value then it lies in  left subtree
        if value < node.value:
            node.left = self.__delete_node(node.left, value)

        # If the value to be delete is greater than the node's value
        # then it lies in right subtree
        elif value > node.value:
            node.right = self.__delete_node(node.right, value)

        # If value is same as node's value, then this is the node
        # to be deleted
        else:
            # Node with only one child or no child
            if node.left is None:
                temp = node.right
                node = None
                return temp

            elif node.right is None:
                temp = node.left
                node = None
                return temp

            # Node with two children: Get the inorder successor
            # (smallest in the right subtree)
            temp = self.in_order_successor(node.right)

            # Copy the inorder successor's content to this node
            node.value = temp.value

            # Delete the inorder successor
            node.right = self.__delete_node(node.right, temp.value)

        return node

    def in_order_successor(self, node):
        current = node
        # loop down to find the leftmost leaf
        while current.left:
            current = current.left

        return current

    def lookup(self, value) -> bool:
        if not value or not self.root:
            return False

        current_node = self.root
        while current_node:
            if value < current_node.value:
                current_node = current_node.left
            elif value > current_node.value:
                current_node = current_node.right
            else:
                return True

        return False

    def breadth_first_search(self) -> List[Any]:
        output = []
        queue = deque()

        queue.append(self.root)
        while len(queue) > 0:
            current = queue.popleft()
            output.append(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

        return output

    def depth_first_search(self, traversal="in_order") -> List[Any]:
        if traversal not in self.__TRAVERSAL_TYPES:
            raise Exception("Traversal Error! Available traversals: in_order, pre_order, post_order.")
        if traversal == "in_order":
            return self.__depth_first_search_inorder(self.root, [])
        elif traversal == "pre_order":
            return self.__depth_first_search_preorder(self.root, [])
        elif traversal == "post_order":
            return self.__depth_first_search_postorder(self.root, [])

    def __depth_first_search_inorder(self, node, output):
        if node.left:
            self.__depth_first_search_inorder(node.left, output)
        output.append(node.value)
        if node.right:
            self.__depth_first_search_inorder(node.right, output)
        return output

    def __depth_first_search_preorder(self, node, output):
        output.append(node.value)
        if node.left:
            self.__depth_first_search_preorder(node.left, output)
        if node.right:
            self.__depth_first_search_preorder(node.right, output)
        return output

    def __depth_first_search_postorder(self, node, output):
        if node.right:
            self.__depth_first_search_postorder(node.right, output)
        if node.left:
            self.__depth_first_search_postorder(node.left, output)
        output.append(node.value)
        return output
