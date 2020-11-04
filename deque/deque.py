from typing import Any
from doubly_linked_list.doubly_linked_list import LinkedList


class Deque:
    def __init__(self):
        self.__contents = LinkedList()

    def __str__(self):
        return str(self.__contents)

    def size(self):
        return self.__contents.size()

    def append(self, value) -> None:
        self.__contents.append(value)

    def append_left(self, value) -> None:
        self.__contents.append_left(value)

    def extend(self, iterable) -> None:
        if isinstance(iterable, list) or isinstance(iterable, tuple):
            for item in iterable:
                self.__contents.append(item)
        elif isinstance(iterable, dict):
            for key in iterable:
                self.__contents.append(iterable[key])

    def extend_left(self, iterable) -> None:
        if isinstance(iterable, list) or isinstance(iterable, tuple):
            for item in reversed(iterable):
                self.__contents.append_left(item)
        elif isinstance(iterable, dict):
            for key in reversed(iterable):
                self.__contents.append_left(iterable[key])

    def pop(self) -> Any:
        return self.__contents.pop()

    def pop_left(self) -> Any:
        return self.__contents.pop_left()

    def remove(self, value) -> Any:
        return self.__contents.remove_value(value)

    def reverse(self) -> Any:
        return self.__contents.reverse()
