from collections import deque
from typing import Dict, Any


class Graph:
    adjacent_list: Dict[Any, Any]

    def __init__(self):
        self.number_of_nodes = 0
        self.adjacent_list = {}

    def __str__(self):
        output = ""
        for node in self.adjacent_list:
            output += node + " --> "
            for neighbor in self.adjacent_list[node]:
                output += str(neighbor) + " "
            output += "\n"

        return output.rstrip("\n")

    def add_vertex(self, node):
        if node not in self.adjacent_list:
            self.adjacent_list[node] = []
            self.number_of_nodes += 1

    def add_edge(self, node1, node2):
        try:
            self.adjacent_list[node1].append(node2)
            self.adjacent_list[node2].append(node1)
        except KeyError:
            raise Exception("At least one of the nodes doen't exist.")

    def breadth_first_search(self, node):
        visited = {}
        output = []
        q = deque()

        q.append(node)
        visited[node] = True
        while len(q) > 0:
            current = q.popleft()
            output.append(current)
            for neighbor in self.adjacent_list[current]:
                if neighbor not in visited:
                    visited[neighbor] = True
                    q.append(neighbor)

        return output

    def depth_first_search(self, node, visited=None):
        if visited is None:
            visited = {}
        output = []
        if node not in visited:
            visited[node] = True
            output += [node]
        for neighbor in self.adjacent_list[node]:
            if neighbor not in visited:
                output += self.depth_first_search(neighbor, visited)
        return output

    def shortest_path(self, start_node, end_node):
        if start_node == end_node:
            return 0
        visited = {}
        queue = deque()

        visited[start_node] = True
        queue.append([start_node, 0])
        while len(queue) > 0:
            current, distance = queue.popleft()
            for neighbor in self.adjacent_list[current]:
                if neighbor == end_node:
                    return distance + 1
                if neighbor not in visited:
                    visited[neighbor] = True
                    queue.append([neighbor, distance+1])

        return -1
