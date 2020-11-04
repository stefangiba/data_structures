from collections import deque
from typing import List, Any

TRAVERSAL_TYPES = ["in_order", "pre_order", "post_order"]


class Node:
    def __init__(self, value, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


class BST:
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

    def insert(self, value) -> 'BST':
        if not self.root:
            self.root = Node(value)
            return self

        current_node = self.root
        new_node = Node(value)
        while True:
            if new_node.value < current_node.value:
                if not current_node.left:
                    current_node.left = new_node
                    return self
                current_node = current_node.left
            else:
                if not current_node.right:
                    current_node.right = new_node
                    return self
                current_node = current_node.right

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
        if traversal not in TRAVERSAL_TYPES:
            raise Exception("Traversal Error! Available traversals: in_order, pre_order, post_order.")
        if traversal == "in_order":
            return self._depth_first_search_inorder(self.root, [])
        elif traversal == "pre_order":
            return self._depth_first_search_preorder(self.root, [])
        elif traversal == "post_order":
            return self._depth_first_search_postorder(self.root, [])

    def _depth_first_search_inorder(self, node, output):
        if node.left:
            self._depth_first_search_inorder(node.left, output)
        output.append(node.value)
        if node.right:
            self._depth_first_search_inorder(node.right, output)
        return output

    def _depth_first_search_preorder(self, node, output):
        output.append(node.value)
        if node.left:
            self._depth_first_search_preorder(node.left, output)
        if node.right:
            self._depth_first_search_preorder(node.right, output)
        return output

    def _depth_first_search_postorder(self, node, output):
        if node.right:
            self._depth_first_search_postorder(node.right, output)
        if node.left:
            self._depth_first_search_postorder(node.left, output)
        output.append(node.value)
        return output

