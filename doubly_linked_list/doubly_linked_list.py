from typing import Any


class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


class LinkedList:
    def __init__(self, value=None):
        if value:
            self.__length = 1
            self.__head = Node(value)
            self.__tail = self.__head
        else:
            self.__length = 0
            self.__head = None
            self.__tail = None

    def __str__(self):
        output = ""
        if not self.__head:
            return 'Empty List'
        else:
            current = self.__head
            while current:
                output += str(current.value) + " <-> "
                current = current.next
            return output.rstrip(" <-> ")

    def size(self):
        return self.__length

    def get_head(self):
        return self.__head

    def get_tail(self):
        return self.__tail

    def is_empty(self):
        if self.__length > 0:
            return False
        else:
            return True

    def append(self, value) -> None:
        if not self.__head:
            self.__head = Node(value)
            self.__tail = self.__head
            self.__length += 1
            return None

        new_node = Node(value)
        temp = self.__tail
        self.__tail.next = new_node
        self.__tail = new_node
        self.__tail.prev = temp
        self.__length += 1

    def append_left(self, value) -> None:
        if not self.__head:
            self.append(value)
            return None

        new_node = Node(value)
        temp = self.__head
        self.__head.prev = new_node
        self.__head = new_node
        self.__head.next = temp
        self.__length += 1

    def pop(self) -> Any:
        return self.__remove_last_element().value

    def pop_left(self) -> Any:
        return self.__remove_first_element().value

    def contains(self, value):
        current = self.__head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def insert(self, index: int, value) -> None:
        if index < 0:
            raise IndexError("Index out of bounds")

        if index == 0:
            self.append_left(value)
        if index >= self.__length-1:
            self.append(value)

        new_node = Node(value)
        prev_node = self.__traverse_to_index(index-1)
        new_node.next = prev_node.next
        prev_node.next.prev = new_node
        new_node.prev = prev_node
        prev_node.next = new_node
        self.__length += 1

    def remove_at_index(self, index: int) -> Any:
        if self.is_empty():
            self.__raise_empty_list_exception()
        if index >= self.__length or index < 0:
            raise IndexError("Index out of bounds")

        if self.__length == 1:
            removed = self.__remove_length_one()
            return removed.value

        if index == 0:
            removed = self.__remove_first_element()
            return removed.value

        if index == self.__length-1:
            removed = self.__remove_last_element()
            return removed.value

        prev_node = self.__traverse_to_index(index-1)
        to_remove = prev_node.next
        prev_node.next = prev_node.next.next
        prev_node.next.prev = prev_node
        to_remove.prev = None
        to_remove.next = None
        self.__length -= 1
        return to_remove.value

    def remove_value(self, value) -> Any:
        if self.is_empty():
            self.__raise_empty_list_exception()

        if self.__length == 1:
            removed = self.__remove_length_one()
            return removed.value

        if self.__head.value == value:
            removed = self.__remove_first_element()
            return removed.value

        if self.__tail.value == value:
            removed = self.__remove_last_element()
            return removed.value

        current = self.__head
        while current.next:
            if current.next.value == value:
                to_remove = current.next
                current.next = current.next.next
                current.next.prev = current
                to_remove.next = None
                to_remove.prev = None
                self.__length -= 1
                return to_remove.value
            current = current.next

    def reverse(self) -> None:
        temp = self.__head
        self.__head = self.__tail
        current = self.__tail
        while current:
            prev = current.prev
            current.prev = current.next
            current.next = prev
            current = current.next
        self.__tail = temp

    def __remove_length_one(self) -> Node:
        to_remove = self.__head
        self.__head = None
        self.__tail = None
        self.__length -= 1
        return to_remove

    def __remove_first_element(self) -> Node:
        if self.is_empty():
            self.__raise_empty_list_exception()

        if self.__length == 1:
            removed = self.__remove_length_one()
            return removed

        to_remove = self.__head
        self.__head = self.__head.next
        self.__head.prev = None
        self.__length -= 1
        return to_remove

    def __remove_last_element(self) -> Node:
        if self.is_empty():
            self.__raise_empty_list_exception()

        if self.__length == 1:
            removed = self.__remove_first_element()
            return removed

        to_remove = self.__tail
        self.__tail.prev.next = self.__tail.next
        self.__tail = self.__tail.prev
        to_remove.prev = None
        self.__length -= 1
        return to_remove

    def __traverse_to_index(self, index: int) -> Node:
        count = 0
        current_node = self.__head
        while count < index:
            current_node = current_node.next
            count += 1

        return current_node

    def __raise_empty_list_exception(self):
        raise Exception("Empty List: Can't remove from an empty list.")
