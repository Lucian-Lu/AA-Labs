import random
import time
import matplotlib.pyplot as plt
class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def addEdge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))  # For undirected graph, add both directions

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self):
        result = []
        i = 0
        e = 0
        edges = []

        for u in range(self.V):
            for v, w in self.graph[u]:
                edges.append((u, v, w))

        edges.sort(key=lambda item: item[2])

        parent = [i for i in range(self.V)]
        rank = [0] * self.V

        while e < self.V - 1:
            u, v, w = edges[i]
            i += 1
            x = self.find(parent, u)
            y = self.find(parent, v)
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        # print("Edges in the constructed MST")
        for u, v, weight in result:
            minimumCost += weight
            # print("%d -- %d == %d" % (u, v, weight))
        # print("Minimum Spanning Tree", minimumCost)

    def primMST(self):
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        mstSet = [False] * self.V

        key[0] = 0
        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)
            mstSet[u] = True

            for v, w in self.graph[u]:
                if not mstSet[v] and w < key[v]:
                    key[v] = w
                    parent[v] = u

        # print("Edges in the constructed MST")
        minimumCost = 0
        for i in range(1, self.V):
            # print(parent[i], "--", i, "==", key[i])
            minimumCost += key[i]
        # print("Minimum Spanning Tree:", minimumCost)

    def minKey(self, key, mstSet):
        min = float('inf')
        min_index = -1

        for v in range(self.V):
            if key[v] < min and not mstSet[v]:
                min = key[v]
                min_index = v

        return min_index


def generate_graph(vertices=100):
    graph = Graph(vertices)

    for i in range(vertices - 1):
        graph.addEdge(i, i + 1, random.randint(1, vertices))

    for i in range(vertices):
        for j in range(i + 2, vertices):
            if random.random() < 0.5:
                graph.addEdge(i, j, random.randint(1, vertices))

    return graph


def plot_values(vertices_counter, prim_execution_times, kruskal_execution_times, title):
    plt.plot(vertices_counter, prim_execution_times, marker='o', label='Prim')
    plt.plot(vertices_counter, kruskal_execution_times, marker='o', label='Kruskal')
    plt.legend()
    plt.title(title)
    plt.xlabel("Vertices")
    plt.ylabel("Time(s)")
    plt.grid()
    plt.show()


test_cases = int(input("Input the number of test cases: "))
vertices = int(input("Input the number of vertices: "))
increment = int(input("Input the increment for the vertices (added after each test case): "))
execution_times = []
vertices_counter = []

for _ in range(test_cases):
    graph = generate_graph(vertices)
    vertices_counter.append(graph.V)

    start_time = time.perf_counter()
    graph.primMST()
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)

    start_time = time.perf_counter()
    graph.KruskalMST()
    end_time = time.perf_counter()
    execution_times.append(end_time - start_time)

    vertices += increment

prim_execution_times = [time for index, time in enumerate(execution_times) if index % 2 == 0]
kruskal_execution_times = [time for index, time in enumerate(execution_times) if index % 2 != 0]
plot_values(vertices_counter, prim_execution_times, kruskal_execution_times, "Greedy algorithms - Prim & Kruskal")
