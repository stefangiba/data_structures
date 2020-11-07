from typing import List, Any


class Heap:
    __HEAP_TYPES = ["min", "max"]

    def __init__(self, array=None, ordering="min"):
        if ordering not in self.__HEAP_TYPES:
            raise TypeError("A heap can either be a min-heap or a max-heap! Please choose 'min' or 'max' for the "
                            "ordering parameter.")
        self.__type = ordering
        if not array:
            self.__contents = []
        else:
            self.__contents = self.__build_heap(array)

    def __str__(self):
        return str(self.__contents)

    def contents(self) -> List[Any]:
        return self.__contents

    def size(self) -> int:
        return len(self.__contents)

    def type(self) -> str:
        return self.__type

    def push(self, value: Any) -> None:
        self.__contents.append(value)
        self.__heapify(len(self.__contents) - 1)

    def pop(self, index=0) -> None:
        if self.__type == "min":
            heapify_node = self.__min_heapify
        elif self.__type == "max":
            heapify_node = self.__max_heapify

        self.__contents[index] = self.__contents[-1]
        self.__contents.pop(index)
        heapify_node(self.__contents, 0)

    def remove(self, value: Any) -> None:
        if self.__type == "min":
            heapify_node = self.__min_heapify
        elif self.__type == "max":
            heapify_node = self.__max_heapify

        index = self.__contents.index(value)
        self.__contents[index] = self.__contents[-1]
        self.__contents.pop(index)
        heapify_node(self.__contents, 0)

    def peek(self) -> Any:
        return self.__contents[0]

    def __build_heap(self, array: List[Any]) -> List[Any]:
        if self.__type == "min":
            heapify = self.__min_heapify
        elif self.__type == "max":
            heapify = self.__max_heapify

        for i in reversed(range(len(array) // 2)):
            heapify(array, i)

        return array

    def __min_heapify(self, array: List[Any], index: int) -> None:
        left = 2 * index + 1
        right = 2 * index + 2
        smallest = index

        if left < len(array) and array[left] < array[smallest]:
            smallest = left
        if right < len(array) and array[right] < array[smallest]:
            smallest = right
        if smallest != index:
            array[index], array[smallest] = array[smallest], array[index]
            self.__min_heapify(array, smallest)

    def __max_heapify(self, array: List[Any], index: int) -> None:
        left = 2 * index + 1
        right = 2 * index + 2
        largest = index

        if left < len(array) and array[left] > array[largest]:
            largest = left
        if right < len(array) and array[right] > array[largest]:
            largest = right
        if largest != index:
            array[index], array[largest] = array[largest], array[index]
            self.__max_heapify(array, largest)

    def __heapify(self, index) -> None:
        parent = (index - 1) // 2

        if parent >= 0:
            if self.__type == "min":
                if self.__contents[index] < self.__contents[parent]:
                    self.__contents[index], self.__contents[parent] = self.__contents[parent], self.__contents[index]
                    self.__heapify(parent)
            if self.__type == "max":
                if self.__contents[index] > self.__contents[parent]:
                    self.__contents[index], self.__contents[parent] = self.__contents[parent], self.__contents[index]
                    self.__heapify(parent)
