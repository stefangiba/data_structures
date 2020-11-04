from deque.deque import Deque

deque = Deque()
deque.append(1)
deque.append(2)
deque.append(3)
deque.append(4)
deque.append(5)
deque.append_left(6)
deque.append_left(7)

print(deque)
print(deque.size())

deque.pop()
print(deque)
print(deque.size())

deque.pop_left()
print(deque)
print(deque.size())

deque.remove(3)
print(deque)
print(deque.size())

deque.reverse()
print(deque)

deque.extend([25, 50, 100])
print(deque)

deque.extend_left({'da': 1, 'nu': 0})
print(deque)
