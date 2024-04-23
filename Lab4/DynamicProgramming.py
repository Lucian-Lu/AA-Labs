import time
import random
import matplotlib.pyplot as plt

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printSolutionDijkstra(self, dist):
        print("Dijkstra's Algorithm:")
        print("Vertex \t Distance from Source")
        for node in range(self.V):
            print(node, "\t\t", dist[node])

    def printSolutionFloyd(self, dist):
        print("\nFloyd-Warshall Algorithm:")
        print("Following matrix shows the shortest distances between every pair of vertices")
        for i in range(self.V):
            for j in range(self.V):
                if dist[i][j] == float('inf'):
                    print("%7s" % ("INF"), end=" ")
                else:
                    print("%7d\t" % (dist[i][j]), end=' ')
                if j == self.V - 1:
                    print()

    def dijkstra(self, src):
        dist = [float('inf')] * self.V
        dist[src] = 0
        sptSet = [False] * self.V

        for _ in range(self.V):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.V):
                if not sptSet[v] and self.graph[u][v] > 0 and dist[u] + self.graph[u][v] < dist[v]:
                    dist[v] = dist[u] + self.graph[u][v]

        # self.printSolutionDijkstra(dist)

    def floydWarshall(self):
        dist = [[float('inf') for _ in range(self.V)] for _ in range(self.V)]
        for i in range(self.V):
            for j in range(self.V):
                if i == j:
                    dist[i][j] = 0
                else:
                    if self.graph[i][j] != 0:
                        dist[i][j] = self.graph[i][j]

        for k in range(self.V):
            for i in range(self.V):
                for j in range(self.V):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]

        # self.printSolutionFloyd(dist)

    def minDistance(self, dist, sptSet):
        min_val = float('inf')
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_val and not sptSet[v]:
                min_val = dist[v]
                min_index = v

        return min_index

def generate_sparse_graph(vertices=100):
    graph = Graph(vertices)
    for i in range(vertices):
        for j in range(vertices):
            if i != j and random.random() <= 0.2:
                graph.graph[i][j] = random.randint(1, 1000)

    return graph

def generate_dense_graph(vertices=100):
    graph = Graph(vertices)
    for i in range(vertices):
        for j in range(vertices):
            if i != j and random.random() <= 0.8:
                graph.graph[i][j] = random.randint(1, 1000)

    return graph


def plot_values(vertices_counter, dijkstra_execution_times, floyd_execution_times, title):
    plt.plot(vertices_counter, dijkstra_execution_times, marker='o', label='Dijkstra')
    plt.plot(vertices_counter, floyd_execution_times, marker='o', label='Floyd')
    plt.legend()
    plt.title(title)
    plt.xlabel("Vertices")
    plt.ylabel("Time(s)")
    plt.grid()
    plt.show()


test_cases = int(input("Input the number of test cases: "))
vertices = int(input("Input the number of vertices: "))
increment = int(input("Input the increment for the vertices (added after each test case): "))

execution_times_sparse = []
vertices_counter_sparse = []
execution_times_dense = []
vertices_counter_dense = []

for _ in range(test_cases):
    graph = generate_sparse_graph(vertices)
    vertices_counter_sparse.append(graph.V)

    start_time = time.perf_counter()
    graph.dijkstra(0)
    end_time = time.perf_counter()
    execution_times_sparse.append(end_time - start_time)

    start_time = time.perf_counter()
    graph.floydWarshall()
    end_time = time.perf_counter()
    execution_times_sparse.append(end_time - start_time)

    graph2 = generate_dense_graph(vertices)
    vertices_counter_dense.append(graph2.V)

    start_time = time.perf_counter()
    graph2.dijkstra(0)
    end_time = time.perf_counter()
    execution_times_dense.append(end_time - start_time)

    start_time = time.perf_counter()
    graph2.floydWarshall()
    end_time = time.perf_counter()
    execution_times_dense.append(end_time - start_time)

    vertices += increment

dijkstra_execution_times_sparse = [time for index, time in enumerate(execution_times_sparse) if index % 2 == 0]
floyd_execution_times_sparse = [time for index, time in enumerate(execution_times_sparse) if index % 2 != 0]
dijkstra_execution_times_dense = [time for index, time in enumerate(execution_times_dense) if index % 2 == 0]
floyd_execution_times_dense = [time for index, time in enumerate(execution_times_dense) if index % 2 != 0]

plot_values(vertices_counter_sparse, dijkstra_execution_times_sparse, floyd_execution_times_sparse, "Sparse Graph")
plot_values(vertices_counter_dense, dijkstra_execution_times_dense, floyd_execution_times_dense, "Dense Graph")

