from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if not value:
            self.__length = 0
            self.__head = None
            self.__tail = None
        else:
            self.__head = Node(value)
            self.__tail = self.__head
            self.__length = 1

    def __str__(self):
        output = ""
        current = self.__head
        while current:
            output += str(current.value) + " -> "
            current = current.next

        return output.rstrip(" -> ")

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def size(self):
        return self.__length

    def contains(self, value) -> bool:
        current = self.__head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def is_empty(self) -> bool:
        return self.__length == 0

    def pop(self) -> Any:
        return self.remove_at_index(self.__length - 1)

    def pop_left(self) -> Any:
        return self.remove_at_index(0)

    def append(self, value) -> None:
        new_node = Node(value)
        if not self.__head:
            self.__head = new_node
            self.__tail = self.__head
            self.__length += 1
            return None
        self.__tail.next = new_node
        self.__tail = new_node
        new_node.next = None
        self.__length += 1

    def append_left(self, value) -> None:
        if not self.__head:
            self.append(value)
            return None
        new_node = Node(value)
        new_node.next = self.__head
        self.__head = new_node
        self.__length += 1

    def insert(self, index, value) -> None:
        # Handling edge cases
        if index == 0:
            self.append_left(value)
            return None
        if index >= self.__length:
            self.append(value)
            return None

        new_node = Node(value)
        node = self.__traverse_to_index(index-1)
        new_node.next = node.next
        node.next = new_node
        self.__length += 1

    def remove_at_index(self, index: int) -> Any:
        # Checking index for abnormal inputs
        if index >= self.__length or index < 0:
            raise IndexError("Index out of bounds!")

        # Edge case when index equals 0
        if index == 0:
            to_remove = self.__head
            self.__head = self.__head.next
            return to_remove.value

        prev_node = self.__traverse_to_index(index-1)
        to_remove = prev_node.next
        prev_node.next = prev_node.next.next
        self.__length -= 1

        return to_remove.value

    def remove_value(self, value) -> Node:
        if self.__head.value == value:
            removed = self.remove_at_index(index=0)
            return removed
        if self.__tail.value == value:
            removed = self.remove_at_index(index=self.__length-1)
            return removed

        current = self.__head
        while current:
            if current.next.value == value:
                to_remove = current.next
                current.next = current.next.next
                self.__length -= 1
                return to_remove.value
            current = current.next

    def reverse(self):
        prev_node = None
        current_node = self.__head

        self.__tail = current_node
        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.__head = prev_node

    def __traverse_to_index(self, index):
        counter = 0
        current_node = self.__head
        while counter < index:
            current_node = current_node.next
            counter += 1

        return current_node
