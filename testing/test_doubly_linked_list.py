from doubly_linked_list.doubly_linked_list import LinkedList

linked_list = LinkedList()
linked_list.append(1)
print(linked_list)
linked_list.remove_value(1)
print(linked_list)
linked_list.append(2)
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.append_left(10)

print(linked_list)

linked_list.insert(3, 7)
print(linked_list)

linked_list.reverse()
print(linked_list)

linked_list.remove_at_index(linked_list.size()-1)
print(linked_list)

linked_list.remove_value(7)
print(linked_list)

print(linked_list.contains(25))

linked_list.reverse()
print(linked_list)

print(linked_list.pop())
print(linked_list)

print(linked_list.pop_left())
print(linked_list)
