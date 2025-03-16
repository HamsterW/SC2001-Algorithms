### We can code our own minimising heap but also python has a heapq module already lmao ###
import math
from heapq import heapify, heappush, heappop

# PriorityQueueArray Class: implement priority queue using an array
class PriorityQueueArray:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def insert(self, node): # node = (prority, vertex)
        self.queue.append(node)
        self.queue.sort(key=lambda x: x[0], reverse=True)
    
    def pop(self):
        return self.queue.pop()
    
    def remove(self, vertex):
        for i in range(len(self.queue)):
            if self.queue[i][1] == vertex:
                self.queue.pop(i)
                break
    
    def __str__(self):
        return str(self.queue)

# Graph Class: represents a graph using adjancency matrix/adjacency list
class Graph:
    def __init__(self, size):
        self.V = size
        self.E = 0
    
    def __str__(self):
        return f"Graph with {self.V} vertices and {self.E} edges"
    
# AdjMatrix Class: represents a graph using an adjacency matrix
class AdjMatrix(Graph):
    def __init__(self, size):
        super().__init__(size)
        self.graph = [[-1] * size for _ in range(size)]
    
    def add_edge(self, v1, v2, weight):
        assert v1 != v2, \
            "cannot add edge between the same vertex"
        assert 0 <= v1 < self.V, \
            "v1 is out of bounds"
        assert 0 <= v2 < self.V, \
            "v2 is out of bounds"
        assert 0 <= weight, \
            "weight must be non-negative"

        self.graph[v1][v2] = weight
        self.E += 1
    
    # (a) Dijkstra's Algorithm using Adjancency Matrix and Priority Queue using Array
    def dijkstra(self, start):
        # Initialise all starting values
        distance = [math.inf for _ in range(self.V)]
        pi = [-1 for _ in range(self.V)]
        visited = [0 for _ in range(self.V)]

        distance[start] = 0

        # Create a priority queue and insert all vertices
        pq = PriorityQueueArray()
        for i in range(self.V):
            pq.insert((distance[i], i))
        
        # Actual Dijkstra's Algorithm
        while not pq.isEmpty():
            _, u = pq.pop()
            visited[u] = 1

            for v, w in enumerate(self.graph[u]):
                if visited[v] == 0 and w != -1 and distance[u] + w < distance[v]:
                    pq.remove(v)
                    distance[v] = distance[u] + w
                    pi[v] = u
                    pq.insert((distance[v], v))

        return distance

# AdjList Class: represents a graph using an adjacency list
class AdjList(Graph):
    def __init__(self, size):
        super().__init__(size)
        self.graph = [[] for _ in range(size)]
    
    def add_edge(self, v1, v2, weight):
        assert v1 != v2, \
            "cannot add edge between the same vertex"
        assert 0 <= v1 < self.V, \
            "v1 is out of bounds"
        assert 0 <= v2 < self.V, \
            "v2 is out of bounds"
        assert 0 <= weight, \
            "weight must be non-negative"
        
        self.graph[v1].append((v2, weight))
        self.E += 1
    
    # (b) Dijkstra's Algorithm using Adjancency List and Priority Queue using Minimising Heap
    def dijkstra(self, start):
        # Initialise all starting values
        distance = [math.inf for _ in range(self.V)]
        pi = [-1 for _ in range(self.V)]
        visited = [0 for _ in range(self.V)]

        distance[start] = 0

        # Create a priority queue and insert all vertices
        pq = []
        for i in range(self.V):
            heappush(pq, (distance[i], i))
        
        # Actual Dijkstra's Algorithm
        while pq:
            _, u = heappop(pq)
            visited[u] = 1

            for v, w in self.graph[u]:
                if visited[v] == 0 and distance[u] + w < distance[v]:
                    distance[v] = distance[u] + w
                    pi[v] = u
                    heappush(pq, (distance[v], v))

        return distance