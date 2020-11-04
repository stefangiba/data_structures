from typing import Any
from singly_linked_list.singly_linked_list import LinkedList


class HashTable:
    def __init__(self, size):
        self.__data = [LinkedList() for i in range(size)]
        self.__size = 0

    def __hash(self, key) -> int:
        hashed_value = 0
        if type(key) != 'string':
            key = str(key)
        for i in range(len(key)):
            hashed_value = (hashed_value + ord(key[i]) * i) % len(self.__data)
        return hashed_value

    def set(self, key, value) -> None:
        hashed_key = self.__hash(key)
        if not self.__data[hashed_key]:
            self.__data[hashed_key] = LinkedList()
        self.__data[hashed_key].append((key, value))
        self.__size += 1

    def get(self, key) -> Any:
        hashed_key = self.__hash(key)
        bucket = self.__data[hashed_key]
        if bucket:
            value_at_key = self.__get_value_at_key(bucket, key)
            if value_at_key:
                return value_at_key
            else:
                raise KeyError(key)
        else:
            raise KeyError(key)

    def keys(self):
        if self.__size == 0:
            return []
        keys = []
        for bucket in self.__data:
            if bucket:
                keys += self.__get(bucket, what="keys")
        return keys

    def values(self):
        if self.__size == 0:
            return []
        values = []
        for bucket in self.__data:
            if bucket:
                values += self.__get(bucket, what="values")
        return values

    def __get_value_at_key(self, bucket: LinkedList, key):
        current = bucket.get_head()
        while current:
            if current.value[0] == key:
                return current.value[1]
            current = current.next
        return None

    def __get(self, bucket: LinkedList, what):
        output = []
        current = bucket.get_head()
        while current:
            if what == "keys":
                output.append(current.value[0])
            elif what == "values":
                output.append(current.value[1])
            current = current.next
        return output
