from heap.heap import Heap
import heapq

arr = [10, 5, 3, 2, 4]
heap = Heap(arr, "max")
print(heap)

heap.push(15)
print(heap)

heap.pop()
print(heap)

heap.remove(3)
print(heap)

heap.push(7)
print(heap)

heap.push(8)
print(heap)

print(heap.peek())
