import random
import time
from collections import deque
import matplotlib.pyplot as plt


class Graph:
    def __init__(self):
        self.edges = {}

    def addEdge(self, a, b):
        if a not in self.edges:
            self.edges[a] = []
        self.edges[a].append(b)

    def bfs(self, startNode):
        if startNode not in self.edges:
            return "No such Node"

        visited = set()
        queue = deque([startNode])

        while queue:
            node = queue.popleft()
            visited.add(node)

            for neighbor in self.edges[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

    def dfs(self, startNode):
        visited = set()
        stack = deque([startNode])

        while stack:
            node = stack.pop()
            if node in visited:
                continue
            if node not in self.edges:
                continue
            visited.add(node)
            for neighbor in reversed(self.edges[node]):
                if neighbor not in visited:
                    stack.append(neighbor)


def generate_graph(nodes):
    graph = Graph()
    for i in range(nodes - 1):
        graph.addEdge(i, i+1)
        graph.addEdge(i+1, i)
        if random.random() < 0.1:
            graph.addEdge(i, random.choice(list(graph.edges.keys())))
        elif random.random() < 0.2:
            graph.addEdge(i + 1, random.choice(list(graph.edges.keys())))
        elif random.random() < 0.3:
            graph.addEdge(random.choice(list(graph.edges.keys())), random.choice(list(graph.edges.keys())))

    for key in graph.edges:
        graph.edges[key] = list(set(graph.edges[key]))

    return graph


node_count = int(input("Input the number of nodes: "))
increment = int(input("Input the increment for the nodes (added after each test case): "))
test_cases = int(input("Input the number of test cases: "))
execution_times = []
node_counter = []
for i in range(test_cases):
    node_counter.append(node_count)
    graph = generate_graph(node_count)
    start_node = random.randint(0, node_count - 1)

    # Measure BFS execution time
    start_time = time.perf_counter()
    graph.bfs(start_node)
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)

    # Measure DFS execution time
    start_time = time.perf_counter()
    graph.dfs(start_node)
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)

    node_count += increment

bfs_execution_times = [time for index, time in enumerate(execution_times) if index % 2 == 0]
dfs_execution_times = [time for index, time in enumerate(execution_times) if index % 2 != 0]

plt.plot(node_counter, bfs_execution_times, marker='o', label='BFS')
plt.plot(node_counter, dfs_execution_times, marker='o', label='DFS')
plt.legend()
plt.title("Graph algorithms")
plt.xlabel("Nodes")
plt.ylabel("Time(s)")
plt.grid()
plt.show()
