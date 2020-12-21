class UnionFind:

    def __init__(self, capacity: int):
        self.__id = []
        self.__size = []
        self.__large = []
        for i in range(capacity):
            self.__id.append(i)
            self.__size.append(1)
            self.__large.append(i)

    # return the largest element in the component containing element
    def find(self, element):
        return self.__large[self.__root(element)]

    def connected(self, first, second) -> bool:
        return self.__root(first) == self.__root(second)

    def union(self, first, second) -> None:
        first_root = self.__root(first)
        second_root = self.__root(second)

        if first_root == second:
            return

        if self.__size[first_root] < self.__size[second_root]:
            self.__id[first_root] = second_root
            self.__size[second_root] += self.__size[first_root]

            if self.__large[first_root] > self.__large[second_root]:
                self.__large[second_root] = self.__large[first_root]
        else:
            self.__id[second_root] = first_root
            self.__size[first_root] += self.__size[second_root]
            if self.__large[second_root] > self.__large[first_root]:
                self.__large[first_root] = self.__large[second_root]

    def __root(self, index: int) -> int:
        while index != self.__id[index]:
            self.__id[index] = self.__id[self.__id[index]]  # path compression
            index = self.__id[index]

        return index


union_find = UnionFind(10)

union_find.union(1, 2)
union_find.union(3, 4)
union_find.union(3, 5)
union_find.union(5, 9)
union_find.union(1, 3)
print(union_find.connected(1, 9))
print(union_find.find(3))
